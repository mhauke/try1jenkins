import pytest
from src.factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(RecursionError):
        factorial(-1)

