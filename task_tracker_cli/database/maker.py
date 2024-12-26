import json

DATABASE_STRUCTURE = {
    "name": "Task Tracker Database",
    "tasks": [
    ]
}

class DatabaseMaker:
    __database_dict = None

    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.__database_dict = DATABASE_STRUCTURE
    
    def update(self, new_dict):
        if new_dict:
            updated_dict = new_dict
        else:
            updated_dict = self.__database_dict
        with open(self.db_file_path, mode="w", encoding="utf-8") as write_file:
            json.dump(updated_dict, write_file, indent=4)