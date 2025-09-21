from tasks.chapter_01_variables import task03

def test_variables_are_equal():
    assert task03.a == task03.b == task03.c, "a, b, and c should all be equal"

def test_not_none():
    assert task03.a is not None, "a should not be None"
    assert task03.b is not None, "b should not be None"
    assert task03.c is not None, "c should not be None"
