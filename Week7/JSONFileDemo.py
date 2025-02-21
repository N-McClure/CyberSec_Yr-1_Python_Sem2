import json
# def display_json():
#     with open('student1.json') as f:
#         data = json.load(f)
#         # for s in data['students']:
#         #     print(s)

#         print(data)

def get_students_from_json():
    with open(r'E:\1-SC\1-Courses\1-2024-Winter\1-PROG23199\CourseMaterials\Demo\3-Files\JSON\student.json') as f:
        data = json.load(f) # load(): reads json data from json file and converts that into python dictionary
        for s in data['students']: # reads everything as a dictionary and walking through the value for key = 'student'  
            print(s)

        #print(data) # reads everything as a dictionary
def get_courses_from_json():
    with open(r'E:\1-SC\1-Courses\1-2024-Winter\1-PROG23199\CourseMaterials\Demo\3-Files\JSON\student.json') as f:
        data = json.load(f) # load(): reads json data from json file and converts that into python dictionary
        for c in data['courses']: # reads everythhing as a dictionary and walking through the value for key = 'courses'  
            print(c)

        #print(data) # reads everything as a dictionary

def get_student_name_from_json():
    with open(r'E:\1-SC\1-Courses\1-2024-Winter\1-PROG23199\CourseMaterials\Demo\3-Files\JSON\student.json') as f:
        data = json.load(f)
        for s in data['students']:
            print(s['name']) # accessing json data directly using key 

def generate_student_dictionary(name, sid, campus):
    return {'name': name, 'sid': sid, 'campus': campus}

def write_to_json(students):
    with open('student_json.json', 'w') as f:
        json.dump(students, f)

if __name__ == '__main__':
    get_students_from_json()
    get_courses_from_json()
    get_student_name_from_json()
    
    # write to json
    bob = generate_student_dictionary('Bob', 111, 'Oakville')
    alice = generate_student_dictionary('Alice', 222, 'Oakville')
    john = generate_student_dictionary('John', 333, 'Bramption')
    write_to_json([bob, alice, john])
