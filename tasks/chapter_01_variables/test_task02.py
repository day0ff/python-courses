from tasks.chapter_01_variables import task02

def test_a_is_int():
    assert isinstance(task02.a, int), "a should be an integer"

def test_b_is_float():
    assert isinstance(task02.b, float), "b should be a float"

def test_c_is_string():
    assert isinstance(task02.c, str), "c should be a string"

def test_values_are_not_none():
    assert task02.a is not None, "a should not be None"
    assert task02.b is not None, "b should not be None"
    assert task02.c is not None, "c should not be None"
