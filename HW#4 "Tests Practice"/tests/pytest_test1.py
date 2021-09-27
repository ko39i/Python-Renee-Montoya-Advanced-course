import pytest
from functions_to_test import Calculator

def test_add_1():
    assert Calculator.add(2,5) == 7

def test_add_2():
    assert Calculator.add(2, 7) != 7

def test_subtract_1():
    assert Calculator.subtract(82, 5) != 6

def test_subtract_2():
    assert Calculator.subtract(12, 6) == 6

def test_multiply():
    assert Calculator.multiply(6, 6) == 36

@pytest.mark.parametrize("x, y, expected_result", [(10,2, 5),
                                                   (20, -2, -10),
                                                   (10, 10, 1)])
def test_divide_1(x, y, expected_result):
    assert Calculator.divide(x, y) == expected_result

def test_type_error():
    with pytest.raises(TypeError):
        Calculator.divide(3, "2")

