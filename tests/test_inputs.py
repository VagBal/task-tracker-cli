import pytest
from unittest.mock import MagicMock
from task_tracker_cli.inputs.core import Add, Delete, Update, Mark, ListAll, ListDone, ListInProgress

@pytest.fixture
def mock_database():
    return MagicMock()

def test_add_command(mock_database):
    add = Add()
    description = "New Task"
    add.execute(mock_database, description)
    mock_database.create_task.assert_called_once_with(description)

def test_delete_command(mock_database):
    delete = Delete()
    task_id = 1
    delete.execute(mock_database, task_id)
    mock_database.delete_task.assert_called_once_with(task_id)

def test_update_command(mock_database):
    update = Update()
    task_id = 1
    new_description = "Updated Task"
    update.execute(mock_database, task_id, new_description)
    mock_database.update_task.assert_called_once_with(task_id, new_description)

def test_mark_command(mock_database):
    mark = Mark()
    task_id = 1
    new_status = "done"
    mark.execute(mock_database, task_id, new_status)
    mock_database.mark_new_status.assert_called_once_with(task_id, new_status)

def test_listall_command(mock_database):
    list_all = ListAll()
    list_all.execute(mock_database)
    mock_database.list_tasks_by_status.assert_called_once_with()

def test_listdone_command(mock_database):
    list_done = ListDone()
    list_done.execute(mock_database)
    mock_database.list_tasks_by_status.assert_called_once_with("done")

def test_listinprogress_command(mock_database):
    list_in_progress = ListInProgress()
    list_in_progress.execute(mock_database)
    mock_database.list_tasks_by_status.assert_called_once_with("in progress")
