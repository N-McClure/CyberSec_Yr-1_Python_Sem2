print(" --- Friday, February 7th, 2025 | 0800 - 1000 ---")

# Practicing Exception Handling.

if __name__ == "__main__":
    
    # Exception Handling Review (Basic):
    
    # Try Block:
    try:
        num1 = input("Please enter first number: ")
        num2 = input("Please enter second number: ")
        result = int(num1) / int(num2) # Probable to throwing an exception.
        
    # Exception for user entering divisor 0:
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        
    # Exception for non-integer inputs:
    except ValueError:
        print("Error: Both inputs must be integers.")
        
        
    # Exception for any other type of exception:
    except Exception as e:
        print(f"An error occurred: {e}")
        
    else:
        print("No errors occurred...whoohoo!")      
        print(result)  
    
    finally:
        print("This block will always run.")
        
# Custom Exception Handling:
class InvalidMarksError(Exception): # Must Inherit from Exception
    def __init__(self, value):
        self.value = value
        

if __name__ == "__main__":
    try:
        marks = input("Please enter your marks: ")
        if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
            raise InvalidMarksError("Invalid marks. Please enter a number between 0 and 100.")

    except InvalidMarksError as e:
        print(e)
    