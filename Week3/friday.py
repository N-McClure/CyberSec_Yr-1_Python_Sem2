print(" --- Friday, January 24th, 2025 | 0800 - 1100 ---")

# Today's concept is "Method Overloading":

# Imported Libraries:
from multipledispatch import dispatch

class Calculator:
    def add(self, *arg):
        result = 0
        for i in arg:
            result += i
        return result
    
class Computer:
    def __init__(self):
        pass
    
    @dispatch(int, int, int, int) # Four integer type data.
    def add(self, n1, n2, n3, n4):
        print(f" Sum of 4 integers: {n1 + n2 + n3 + n4}")
    
    @dispatch(int, int)
    def add(self, n1, n2): # Integer type data.
        print(f" Sum of 2 intergers: {n1 + n2}")
    
    @dispatch(float, float)
    def add(self, n1, n2): # Float type data.
        print(f" Sum of 2 floats: {n1 + n2}")
    
if __name__ == "__main__":
    calc = Calculator()
    
    # Calling the "add" method with three arguments
    print(calc.add(3, 5, 7))
    
    # Calling the "add" method with two arguments
    print(calc.add(5, 7))
    
    comp = Computer()
    
    comp.add(5, 7)
    comp.add(5.5, 7.5)
    comp.add(5, 7, 8, 9)