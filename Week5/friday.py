print(" --- Friday, February 7th, 2025 | 0800 - 1000 ---")

# Building up on the code we wrote on Wednesday...learning about Set Comprehension now.

def list_comprehensions():
    list = [2,3,4,5]
    print(list)
    
    # TODO: Double values in list without for loop.
    doubled_list = [item * 2 for item in list]
    print(doubled_list)
    
    # TODO: Print EVEN elements of the list:
    even_numbers = [item for item in list if item % 2 == 0]
    print(even_numbers)
    
def isEven(x):
    return True if x % 2 == 0 else False

def isOdd(x):
    return True if x % 2!= 0 else False

def hasUpper(s):
    for c in s:
        if c.isupper():
            return True
    return False

def list_comprehensions2():
    list = [2,3,4,5]
    
    print([x for x in list if isEven(x)])
    print([x for x in list if isOdd(x)])
    
    print([100 for x in list])
    
    print([0 for x in list if isEven(x)])
    print(list)
    
    print([x * 2 if isEven(x) else x * 3 for x in list])
    
    words = ['hello', "HeLlO", "wOrds", "Oranges"]
    print([x.lower() if hasUpper(x) else x.upper() for x in words])
    
def dictionary_comprehensions():
    num_list = [1,2,3,4,5]    
    sq_dict = {num: num ** 2 for num in num_list}
    print(sq_dict)
    
    num_list2 = ('n1', 'n2', 'n3', 'n4', 'n5')
    nums_dict = {num_list2[i]: num_list[i] for i in range(len(num_list2))}
    print(nums_dict)
    
    print({x: len(x) for x in num_list2})
    
    print({k:v for k,v in nums_dict.items() if v >= 3})
    
    print({v:k for k,v in nums_dict.items()})    
    
# All new things below this line:

def set_comprehensions():
    set1 = ([1,2,3,4,5])
    set2 = {i for i in set1}
    
    print(set2)
    
    # TODO: Print a set of the squares for only Odd nums in the set.
    print([x**2 for x in set1 if isOdd(x)])
    
# TODO: Create a class called Student, with a couple of objects, output ID: Name as a dictionary using comprehesion.
class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return self.name
    
    def student_comprehensions():
        students = [Student(101, "John"), Student(102, "Alice"), Student(103, "Bob")]
        student_dict = {student.id: student.name for student in students}
        print(student_dict)
        
# TODO: Create a class called Item, with some objects, output ID, name, and category...then make a collection of a person's favs using comprehension.

class Item():
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
    
    def __str__(self):
        return f"{self.id} - {self.name} - {self.category} - {self.price}"
    
    def item_comprehensions():
        items = [Item(101, "Apple", "Fruit", 1.99), Item(102, "Cheese", "Dairy", 3.50), Item(103, "Carrot", "Vegetable", 0.75), Item(104, "Bacon", "Meat", 4.75)]
        nick_favs = {item.id: item.name for item in items if item.category == "Meat"}
        bob_favs = {item.id: item.name for item in items if item.category == "Fruit"}
        print(f'Nick favs: {nick_favs}')
        print(f'Bob favs: {bob_favs}')
        
        # TODO: output a total cost of the person's favourites using comprehension:
        nick_cost = sum(item.price for item in items if item.id in nick_favs)
        print(f'Total cost of Nick\'s favs: {nick_cost}')
        
        bob_cost = sum(item.price for item in items if item.id in bob_favs)
        print(f'Total cost of Bob\'s favs: {bob_cost}')

if __name__ == "__main__":
    # list_comprehensions()
    # list_comprehensions2()
    # dictionary_comprehensions()
    
    #set_comprehensions()
    #Student.student_comprehensions()
    Item.item_comprehensions()