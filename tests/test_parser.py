import pytest
from argparse import ArgumentParser
from unittest.mock import patch, MagicMock
from task_tracker_cli.parser.core import Parser

@pytest.fixture
def parser():
    return Parser()

def test_parser_add_argument(parser):
    args = parser.parser.parse_args(['-a', 'New Task'])
    assert args.add == 'New Task'
    assert args.delete is None
    assert args.update is None
    assert args.mark is None
    assert args.listall is False
    assert args.listdone is False
    assert args.listip is False

def test_parser_delete_argument(parser):
    args = parser.parser.parse_args(['-d', '1'])
    assert args.add is None
    assert args.delete == '1'
    assert args.update is None
    assert args.mark is None
    assert args.listall is False
    assert args.listdone is False
    assert args.listip is False

def test_parser_update_argument(parser):
    args = parser.parser.parse_args(['-u', '1', 'Updated Task'])
    assert args.add is None
    assert args.delete is None
    assert args.update == ['1', 'Updated Task']
    assert args.mark is None
    assert args.listall is False
    assert args.listdone is False
    assert args.listip is False

def test_parser_mark_argument(parser):
    args = parser.parser.parse_args(['-m', '1', 'done'])
    assert args.add is None
    assert args.delete is None
    assert args.update is None
    assert args.mark == ['1', 'done']
    assert args.listall is False
    assert args.listdone is False
    assert args.listip is False

def test_parser_listall_argument(parser):
    args = parser.parser.parse_args(['-la'])
    assert args.add is None
    assert args.delete is None
    assert args.update is None
    assert args.mark is None
    assert args.listall is True
    assert args.listdone is False
    assert args.listip is False

def test_parser_listdone_argument(parser):
    args = parser.parser.parse_args(['-ld'])
    assert args.add is None
    assert args.delete is None
    assert args.update is None
    assert args.mark is None
    assert args.listall is False
    assert args.listdone is True
    assert args.listip is False

def test_parser_listip_argument(parser):
    args = parser.parser.parse_args(['-lip'])
    assert args.add is None
    assert args.delete is None
    assert args.update is None
    assert args.mark is None
    assert args.listall is False
    assert args.listdone is False
    assert args.listip is True

@patch.object(ArgumentParser, 'parse_args', side_effect=SystemExit("error"))
def test_parse_args_exception(mock_parse_args, parser):
    with pytest.raises(SystemExit):
        parser.parse_args()
