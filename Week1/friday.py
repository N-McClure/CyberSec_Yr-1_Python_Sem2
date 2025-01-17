print(" --- Friday, January 10th, 2025 | 0800 - 1000 ---")

# Review:
class Student:
    
    # Class Level Attributes:
    Campuses = ("Oakville", "Mississauga", "Brampton", "Online") # Made as a Tuple because the options won't ever change.
    count = 0 # Counter for Student Instances created.
    __studentList = None
    
    # Class Level Methods:
    @classmethod
    def get_campuses(cls):
        return cls.Campuses
    
    @staticmethod
    def get_student_list():
        if Student.__studentList is None:
            Student.__studentList = []
        return Student.__studentList
    
    # Instance Level Methods:
    def __init__(self, name, age, grade, campus): # Constructor = the initializer of the instance.
        self.name = name
        self.age = age
        self.grade = grade
        if campus not in Student.Campuses: 
            raise ValueError(f"{campus} is not a valid location.")
        else:
            self.campus = campus
            
        Student.count += 1 # Increment the counter by 1 each time a new Student instance is created.
        
        # Atrributes = the properties of the class (Definitely part of the Student)
        # The pieces above are "Attributes".
        
    # Getters / Accessors:
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade
    
    # Setters / Mutators:
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age
    
    def set_grade(self, grade):
        self.grade = grade
        
def main():
    # Students created:
    
    stud1 = Student("Nick", 20, 92, "Oakville")
    stud2 = Student("Sam", 24, 99, "Brampton")
    stud3 = Student("Petar", 18, 100, "Online")
    
    print("--- Student List ---")
    print(f"Name: {stud1.get_name()}, Age: {stud1.get_age()}, Grade: {stud1.get_grade()}")
    print(f"Name: {stud2.get_name()}, Age: {stud2.get_age()}, Grade: {stud2.get_grade()}")
    print(f"Name: {stud3.get_name()}, Age: {stud3.get_age()}, Grade: {stud3.get_grade()}")
    
    # NEVER DO THIS: print(stud1.name)
    # DO THIS: print(stud1.get_name())
    # REASON: This is more SECURE.
    
    print(Student.get_campuses())
    
    print("Total Students Created and Counted: ", Student.count)
    
    allStudents = Student.get_student_list() # Uses the Static Method.
    allStudents.append(stud1)
    allStudents.append(stud2)
    allStudents.append(stud3)
    
    print(allStudents)
    
# Calling the main method:
main()
        