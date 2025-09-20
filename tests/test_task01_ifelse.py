import pytest
from tasks.task01_ifelse import check_number

def test_positive():
    assert check_number(5) == "positive"

def test_negative():
    assert check_number(-3) == "negative"

def test_zero():
    assert check_number(0) == "zero"

@pytest.mark.parametrize("num", [1, 42, 999])
def test_many_positive(num):
    assert check_number(num) == "positive"

@pytest.mark.parametrize("num", [-1, -100, -999])
def test_many_negative(num):
    assert check_number(num) == "negative"
