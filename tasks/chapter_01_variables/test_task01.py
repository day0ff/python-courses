from tasks.chapter_01_variables import task01

def test_name_is_string():
    assert isinstance(task01.name, str), "name should be a string"

def test_age_is_int():
    assert isinstance(task01.age, int), "age should be an integer"

def test_is_student_is_bool():
    assert isinstance(task01.is_student, bool), "is_student should be a boolean"

def test_name_not_empty():
    assert task01.name.strip() != "", "name should not be empty"

def test_age_non_negative():
    assert task01.age >= 0, "age should not be negative"
