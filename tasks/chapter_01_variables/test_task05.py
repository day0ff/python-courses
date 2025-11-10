from tasks.chapter_01_variables import task05

def test_variables_exist():
    assert hasattr(task05, "x"), "Variable x should exist"
    assert hasattr(task05, "y"), "Variable y should exist"

def test_values_swapped():
    # Initial assignment before swap was x=1, y=2
    assert task05.x == 2, "x should now hold the value 2"
    assert task05.y == 1, "y should now hold the value 1"
