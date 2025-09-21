from tasks.chapter_01_variables import task04

def test_initial_value():
    assert task04.counter == 10, "counter should start at 10"

def test_reset_counter():
    task04.reset_counter_to_zero()
    assert task04.counter == 0, "counter should be 0 after reset"

