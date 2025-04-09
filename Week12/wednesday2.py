# Experimenting with Unit Testing.

# Imported Modules:
from wednesday import Calculator
import pytest
calc = Calculator()

class TestCalculator:
    def testAdd():
        a = 4
        b = 5
        assert calc.add(a,b) == 9
    
    def testSubstract():
        a = 10
        b = 1
        assert calc.subtract(a,b) == 9
    
    def testMultiply():
        a = 4
        b = 5
        assert calc.multiply(a,b) == 20
    
    @pytest.mark.skip # To skip this test
    def testDivision():
        a = 10
        b = 2
        assert calc.add(a,b) == 5