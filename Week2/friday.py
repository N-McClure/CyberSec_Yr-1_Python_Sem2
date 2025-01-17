print(" --- Friday, January 17th, 2025 | 0800 - 1000 --- ")

# Inheritance Basics:
    # - Inheritance allows us to create new classes based on existing ones.
    # - Inheritance enables us to reuse code and reduce redundancy.
    # - Inheritance is a "is-a" relationship.
    # - Parent class: The class from which we inherit.
    # - Child class: The class that inherits from the parent class.
    # - Example: Animal -> Mammal -> Dog -> Labrador
    
# Imported Libraries:
from abc import abstractmethod  
from abc import ABC  

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
        
class Rectangle(Shape):
    def __init__(self, colour, type, length, width):
        super().__init__(colour, type)
        self.length = length
        self.width = width
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
        
class Circle(Shape):
    def __init__(self, colour, type, radius):
        super().__init__(colour, type)
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def get_diameter(self):
        return 2 * self.radius

def main():
    r1 = Rectangle("red", "Rectangle", 10, 5)
    c1 = Circle("Blue", "Oval", 4)
    
    print("--- Rectangle Stats ---")
    print(f'Shape Type: {r1.print_type()}')
    print(f'Length: {r1.get_length()}')
    print(f'Width: {r1.get_width()}')
    
    print("--- Circle Stats ---")
    print(f'Shape Type: {c1.print_type()}')
    print(f'Radius: {c1.get_radius()}')
    print(f'Diameter: {c1.get_diameter()}')
    
main()