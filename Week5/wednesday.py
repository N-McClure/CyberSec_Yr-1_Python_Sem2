print(" --- Wednesday, February 5th, 2025 | 1400 - 1600 ---")

# Doing different types of comprehensions...building on what we learned last friday.

def list_comprehensions():
    list = [2,3,4,5]
    print(list)
    
    # TODO: Double values in list without for loop.
    doubled_list = [item * 2 for item in list]
    print(doubled_list)
    
    # TODO: Print EVEN elements of the list:
    even_numbers = [item for item in list if item % 2 == 0]
    print(even_numbers)
    
# All new things below this line:
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

if __name__ == "__main__":
    list_comprehensions()
    list_comprehensions2()
    dictionary_comprehensions()