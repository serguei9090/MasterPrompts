import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from api import add, subtract, multiply, divide, modulo, cosine, sine
import pytest
import math

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_modulo():
    assert modulo(10, 3) == 1
    with pytest.raises(ValueError):
        modulo(10, 0)

def test_trig():
    assert math.isclose(cosine(0), 1.0)
    assert math.isclose(sine(0), 0.0)
    assert math.isclose(cosine(math.pi), -1.0)
