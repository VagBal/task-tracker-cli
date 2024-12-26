import os.path
import json
from pathlib import Path
import datetime
from enum import Enum
from task_tracker_cli.database.maker import DatabaseMaker
from task_tracker_cli.task.core import Task
from prettytable import PrettyTable
import logging

logging.basicConfig(level=logging.ERROR)

BASE_PATH = Path(__file__).parent
DB_FILE_NAME = "db.json"
DB_FILE_PATH = (BASE_PATH / "../database/db.json").resolve()

class States(Enum):
    INACTIVE = 0
    ACTIVE = 1

class Database:
    # Standard way to make a Singleton
    _instance = None
    __database = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.init_database()
        return cls._instance

    def is_active(self):
        if self.state == States.ACTIVE:
            return True
        return False
    
    def init_database(self):
        # Change state to active
        # Check if there is a json called db.json is exists under database dir if yes load it
        # If not create a new json database and save it to the database/db.json
        self.state = States.ACTIVE
        self.db_maker = DatabaseMaker(DB_FILE_PATH)

        if self.is_db_file_exists() is False:
            self.update_db_file(new_dict=None)
        
        self.load_db_from_db_file(DB_FILE_PATH)

        self.id_counter = self.get_last_id()

    def deactivate(self):
        self.state = States.INACTIVE

    def is_db_file_exists(self):
        if os.path.isfile(DB_FILE_PATH) is True:
            return True
        return False

    def load_db_from_db_file(self, path):
        with open(path, mode="r", encoding="utf-8") as read_file:
            self.__database = json.load(read_file)

    def update_db_file(self, new_dict):
        self.db_maker.update(new_dict)
    
    def create_task(self, description):
        self.id_counter += 1
        task = Task(self.id_counter, description, datetime.datetime.now(), datetime.datetime.now())
        task_dict = task.task_as_dict()
        self.__database["tasks"].append(task_dict)
        
        self.update_db_file(self.__database)

    def delete_task(self, id):
        try:
            self.__database["tasks"] = [task for task in self.__database["tasks"] if task["id"] != id]
            self.update_db_file(self.__database)
            print(f"The Task with id: {id} has been deleted")
        except Exception as e:
            logging.error(f"Error deleting task {id}: {e}")
            print("An error occurred while deleting the task. Please try again.")

    def update_task(self, id, new_description):
        try: 
            task = self.find_task_by_id(id)
            task["description"] = new_description
            task["updatedAt"] = str(datetime.datetime.now())
        except ValueError as e: 
            print(e)

        self.update_db_file(self.__database)

    def mark_new_status(self, id, new_status):
        try: 
            task = self.find_task_by_id(id)
            task["status"] = new_status
            print(f"The Task with id: {id} status changed to {new_status}")
        except ValueError as e: 
            print(e)

        self.update_db_file(self.__database)

    def find_task_by_id(self, id):
        for task in self.__database["tasks"]:
            if task["id"] == id:
                return task
        raise ValueError(f"Task with id {id} not found")

    def list_tasks_by_status(self, status=None):
        tasks = self.__database.get("tasks", [])
        if not tasks:
            print("No tasks available.")
            return

        filtered_tasks = tasks if status is None else [task for task in tasks if task["status"] == status]
        
        if not filtered_tasks:
            print(f"No tasks with status '{status}'." if status else "No tasks available.")
            return

        table = PrettyTable()
        table.field_names = ["id", "description", "status", "createdAt", "updatedAt"]

        for task in filtered_tasks:
            table.add_row([task["id"], task["description"], task["status"], task["createdAt"], task["updatedAt"]])

        print(table)

    def get_last_id(self):
        if self.__database["tasks"]:
            last_task = self.__database["tasks"][-1]
            return last_task["id"]
        else:
            return 0