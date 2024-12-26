from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, database, *args):
        pass

class Add(Command):
    def execute(self, database, description):
        database.create_task(description)

class Delete(Command):
    def execute(self, database, id):
        database.delete_task(id)

class Update(Command):
    def execute(self, database, id, description):
        database.update_task(id, description)

class Mark(Command):
    def execute(self, database, id, new_status):
        database.mark_new_status(id, new_status)

class ListAll(Command):
    def execute(self, database):
        database.list_tasks_by_status()

class ListDone(Command):
    def execute(self, database):
        database.list_tasks_by_status("done")

class ListInProgress(Command):
    def execute(self, database):
        database.list_tasks_by_status("in progress")
