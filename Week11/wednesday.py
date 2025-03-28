# Talking about Filtering:

# NOTE: The built-in filter() function takes 2 args: the function and the sequence.
def isEven(x):
    return True if x % 2 == 0 else False

if __name__ == "__main__":
    # Filter Syntax: map (function or lambda expression, iterables)
    
    # Filter a list for only even numbers:
    print(list(filter(isEven, [4,5,6,7,8,9])))
    
    # TODO: create a filter to find the positive numbers in a set:
    # Create a set of numbers:
    num_set = {1, -2, 3, -4, 5}
    # Filter the list for only positive numbers:
    print(list(filter(lambda x: x > 0, num_set)))
    
    # TODO: create a filter to find the positive and even numbers in a list:
    # Create a list of numbers:
    num_list = [1, -2, 3, -4, 5, 6, -7, 8]
    # Filter the list for only positive and even numbers:
    print(list(filter(lambda x: x > 0 and x % 2 == 0, num_list)))
    
    # TODO: Filter a dictionary of people and ages where peoples age > 18:
    # Create a dictionary of people and ages:
    people_dict = {"Alice": 20, "Alex": 17, "Bob": 20, "Charlie": 19, "Bill": 10}
    # Filter the dictionary for only people who are above 18:
    print({name: age for name, age in people_dict.items() if age > 18})
    