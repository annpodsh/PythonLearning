import pytest
from homework4.tasks.task03 import my_precious_logger


def test_my_precious_logger_common(capsys):
    my_precious_logger("message")
    assert capsys.readouterr().out == "message"


def test_my_precious_logger_error(capsys):
    my_precious_logger("error: message")
    assert capsys.readouterr().err == "error: message"
