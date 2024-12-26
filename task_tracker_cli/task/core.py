from enum import Enum

class TaskStates(Enum):
    DONE = "done"
    IN_PROGRESS = "in progress"

class Task:
    def __init__(self, id, description, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = TaskStates.IN_PROGRESS.value
        self.createdAt = str(createdAt)
        self.updatedAt = str(updatedAt)

    def task_as_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
            }