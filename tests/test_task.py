import pytest
from datetime import datetime
from task_tracker_cli.task.core import Task, TaskStates

def test_task_initialization():
    task_id = 1
    description = "Test Task"
    created_at = datetime.now()
    updated_at = datetime.now()

    task = Task(task_id, description, created_at, updated_at)

    assert task.id == task_id
    assert task.description == description
    assert task.status == TaskStates.IN_PROGRESS.value
    assert task.createdAt == str(created_at)
    assert task.updatedAt == str(updated_at)

def test_task_as_dict():
    task_id = 1
    description = "Test Task"
    created_at = datetime.now()
    updated_at = datetime.now()

    task = Task(task_id, description, created_at, updated_at)
    task_dict = task.task_as_dict()

    assert task_dict["id"] == task_id
    assert task_dict["description"] == description
    assert task_dict["status"] == TaskStates.IN_PROGRESS.value
    assert task_dict["createdAt"] == str(created_at)
    assert task_dict["updatedAt"] == str(updated_at)
