from homework5.tasks.oop_1 import Homework, Student, Teacher
import datetime


def test_homework_creation():
    new_hw = Homework("some task", datetime.timedelta(1))
    assert new_hw.text == "some task"
    new_hw = Homework("some another task", datetime.timedelta(-1))
    assert new_hw.text == "some another task"


def test_homework_true():
    new_hw = Homework("some task", datetime.timedelta(1))
    assert new_hw.is_active()


def test_homework_false():
    new_hw = Homework("some another task", datetime.timedelta(-1))
    assert not new_hw.is_active()


def test_student_creation():
    stud = Student("f_n", "l_n")
    assert stud.first_name == "f_n"
    assert stud.last_name == "l_n"


def test_student_homework_combination_in_time(capsys):
    stud = Student("f_n", "l_n")
    hw = Homework("task text", datetime.timedelta(1))
    hw_done = stud.do_homework(hw)
    assert capsys.readouterr().out == ""
    assert hw_done == hw


def test_student_homework_combination_late(capsys):
    stud = Student("f_n", "l_n")
    hw = Homework("task text", datetime.timedelta(-1))
    hw_done = stud.do_homework(hw)
    assert capsys.readouterr().out == "You are late\n"
    assert hw_done is None


def test_teacher_creation():
    teacher = Teacher("f_n", "l_n")
    assert teacher.first_name == "f_n"
    assert teacher.last_name == "l_n"


def test_teacher_homework_combination():
    teacher = Teacher("f_n", "l_n")
    hw = teacher.create_homework("task text", 3)
    assert hw.is_active()
    assert hw.text == "task text"
