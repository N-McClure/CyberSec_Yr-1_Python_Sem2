# Simple application for the demo of generating documentation:

'''
Methods:
--------
    - add(a,b) : computes the sum of 2 numbers
    - subtract(a,b) : computes the difference of 2 numbers
    - multiply(a,b) : computes the product of 2 numbers
    - divide(a,b) : computes the quotient of 2 numbers
'''

class Calculator:
    # Method: Add
    def add(a:int,b:int) -> int:
        print(a+b)
    
    '''
    Name: Add
    Description: Adds 2 numbers together and outputs the result
    Inputs: Integers 'a' and 'b'
    Outputs: The result of 'a+b'
    '''
    
    def subtract(a:int,b:int) -> int:
        print(a-b)
    
    '''
    Name: Subtract
    Description: Subtracts 2 numbers and outputs the result
    Inputs: Integers 'a' and 'b'
    Outputs: The result of 'a-b'
    '''
    
    def multiply(a:int,b:int) -> int:
        print(a*b)
    
    '''
    Name: Multiply
    Description: Multiplies 2 numbers together and outputs the result
    Inputs: Integers 'a' and 'b'
    Outputs: The result of 'a*b'
    '''
    
    def divide(a:int,b:int) -> float:
        if b == 0:
            raise ZeroDivisionError('Dividing by Zero...')
        print(a/b)
    
    '''
    Name: Divide
    Description: Divides 2 numbers together and outputs the result
    Inputs: Integers 'a' and 'b'
    Outputs: The result of 'a/b'
    Exceptions: ZeroDivision Error
    '''
    
# Main Method:
if __name__ == '__main__':
    calc = Calculator
    
    # Print the documentation for entire Calculator class:
    print(calc.__doc__)