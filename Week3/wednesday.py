print(" --- Wednesday, January 22nd, 2025 | 1400 - 1600 ---")

# Using the base of Last Friday's code to demo Multiple Inheritance:

# Imported Libraries:
from abc import abstractmethod  
from abc import ABC  

# Creation of an Interface:
class Colourable(ABC): # an Interface.
    @abstractmethod
    def colourable():
        pass

class Shape(ABC):
    def __init__(self, colour, type):
        self.colour = colour
        self.type = type
        
    def print_type(self):
        return self.type
    
    # Abstract Method for Child classes to inherit and use:
    @abstractmethod
    def get_area(self):
        pass
    
    # --- Notes On Abstract Classes --- 
    # - Must have atleast one Abstract Method.
    # - May have Concrete methods.
    # - Abstract Classes cannot be instantiated.
    # - All Sub-Classes must implement ALL abstract methods.
        
class Person:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def greeting(self):
        return f'Hello, my name is {self.name}!'
        
class Rectangle(Shape, Person):
    def __init__(self, colour, type, length, width, name):
        Shape.__init__(self, colour, type)
        Person.__init__(self, name)
        self.length = length
        self.width = width
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_area(self):
        return self.length * self.width
    
    def greeting(self):
        return f'Hello from the Shape class!!!...Not a Person!!!'
        
class Circle(Shape):
    

    def __init__(self, colour, type, radius):
        super().__init__(colour, type)
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def get_diameter(self):
        return 2 * self.radius
    
    def get_area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, colour, type, base, height):
        super().__init__(colour, type)
        self.base = base
        self.height = height
        
    def get_base(self):
        return self.base
    
    def get_height(self):
        return self.height
    
    def get_area(self):
        return 0.5 * self.base * self.height

class Furniture:
    def __init__(self,made_of):
        self.made_of = made_of
        
class Table(Furniture, Colourable):
    def __init__(self, made_of, side1, side2, colour):
        super().__init__(made_of)
        self.colour = colour
    
    def get_made_of(self):
        return self.made_of
    
    def get_colour(self):
        return self.colour

def main():
    r1 = Rectangle("red", "Rectangle", 10, 5, 'Nick')
    
    print("--- Rectangle Stats ---")
    print(f'Shape Type: {r1.print_type()}')
    print(f'Length: {r1.get_length()}')
    print(f'Width: {r1.get_width()}')
    print(f'Area: {r1.get_area()}')
    print(f'Creator: {r1.get_name()}')

    
    
main()