import pytest
from Untitled import Calculator

#Fixture to create an instance of the Calculator class
@pytest.fixture
def calculator():
    return Calculator()

#Test case for the add method
def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0,0) == 0
    assert calculator.add(-5, -7) == -12

# Test case for the div method
def test_div(calculator):
    assert calculator.division(4, 2) == 2
    assert calculator.division(-1, 1) == -1
    assert calculator.division(0, 5) == 0

# Test case for division by zero
def test_div_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.div(10, 0)



#Test case for the Division method
#def test_div(calculator):
    #assert calculator.division(2, 3) == 5
    #assert calculator.division(-1, 1) == 0
    #assert calculator.division(0,0) == 0
    #assert calculator.division(-5, -7) == -12
