# Imported Libraries:
from dataclasses import dataclass
from dataclasses import field

@dataclass
class Student:
    # In dataclass, __init__() method is not required.
    # Type hint for each attribute is required.
    sid : int
    name : str
    semester : int
    grade : float = 0.0 # setting the default value.
    campus : str = 'Oakville'
    
    # NOTE: Variables with defalut values MUST be AFTER those without...as seen above.
    
    # Other regular instance methods can be added in dataclass.
    def student_info(self):
        return f"Name: {self.name} and Grade: {self.grade}"
    
    # Uses the __post_init__() to customize more attributes.
    def __post_init__(self):
        self.total_grade = self.grade*self.semester
    
def main():
    stud1 = Student(0, "Stew Dent", 3.9, 4)
    stud2 = Student(1, "Stuart D. Ent", 2.8, 2)
    
    print(stud1) # __str__() magic method is implemented here by default in dataclass
    print(stud1 == stud2)  # __eq__() magic method is implemented here by default in dataclass
    print(stud2.student_info()) # Regular Instance methods work too.
    print(stud1.total_grade)
    print(stud2.total_grade) 
    
main()