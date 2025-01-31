print(" --- Friday, January 31st, 2025 | 0800 - 1000 ---")

# Talking about Comprehensions:

# List Comprehension:
def list_comprehensions():
    list = [2,3,4,5]
    print(list)
    
    # TODO: Double values in list without for loop.
    doubled_list = [item * 2 for item in list]
    print(doubled_list)
    
    # TODO: Print EVEN elements of the list:
    even_numbers = [item for item in list if item % 2 == 0]
    print(even_numbers)
    
if __name__ == "__main__":
    list_comprehensions()