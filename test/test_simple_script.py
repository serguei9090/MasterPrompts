from test.simple_script import get_random_number, add, multiply, square

def test_get_random_number():
    num = get_random_number()
    assert 1 <= num <= 100

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(0, 5) == 0

def test_square():
    assert square(12) == 144
    assert square(0) == 0
