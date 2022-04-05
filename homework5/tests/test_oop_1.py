from homework5.tasks.oop_1 import Homework, Student, Teacher
import datetime

some_task_in_time_hw = Homework("some task", datetime.timedelta(1))
some_another_task_late_hw = Homework("some another task", datetime.timedelta(-1))
stud = Student("f_n", "l_n")
teacher = Teacher("f_n", "l_n")


def test_homework_creation():
    assert some_task_in_time_hw.text == "some task"
    assert some_another_task_late_hw.text == "some another task"


def test_homework_true():
    assert some_task_in_time_hw.is_active()


def test_homework_false():
    assert not some_another_task_late_hw.is_active()


def test_student_creation():
    assert stud.first_name == "f_n"
    assert stud.last_name == "l_n"


def test_student_homework_combination_in_time(capsys):
    hw_done = stud.do_homework(some_task_in_time_hw)
    assert capsys.readouterr().out == ""
    assert hw_done == some_task_in_time_hw


def test_student_homework_combination_late(capsys):
    hw_done = stud.do_homework(some_another_task_late_hw)
    assert capsys.readouterr().out == "You are late\n"
    assert hw_done is None


def test_teacher_creation():
    assert teacher.first_name == "f_n"
    assert teacher.last_name == "l_n"


def test_teacher_homework_combination():
    hw = teacher.create_homework("task text", 3)
    assert hw.is_active()
    assert hw.text == "task text"
