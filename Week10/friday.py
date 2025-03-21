# Started talking about "Large-Scale Development Essentials".

# Anonymous Functions / 'Lambda Functions':

# Regular function to square a variable:
def square(x):
    print(x ** 2)
    
# Regular function to multipy two values:
def multiply(x, y):
    print(x * y)


if __name__ == '__main__':
    square(5) # Calls and uses basic square function.
    
    # Lambda function to square a variable:
    square_lambda = lambda x: x ** 2
    print(square_lambda(5)) # Calls and uses Lambda expression to square.
    
    multiply(5,3) # Calls and uses basic multiply function.
    
    # Lambda function to multiply two values:
    multiply_lambda = lambda x, y: x * y
    print(multiply_lambda(5, 3)) # Calls and uses Lambda expression to multiply.
    
    # TODO: Lambda function to convert a string to Uppercase:
    con_to_upper = lambda x: x.upper()
    print(con_to_upper('hello')) # Calls and uses Lambda expression to convert string to uppercase.
    
    # TODO: Lambda function to greet a user with inputted name:
    greet_user = lambda name: f'Hello, {name}!'
    print(greet_user('Bobbert')) # Calls and uses Lambda expression to greet a user.
    
    # List Comprehension example with Lambda:
    # TODO: Lambda function take the values of a list and multiply each value by 10:
    my_list = [lambda arg = x : arg * 10 for x in range(1,5)]
    for i in my_list:
        print(i()) # Calls and uses Lambda expression to multiply each value by 10.
    
    # TODO: Lambda function to check if a number is "Even":
    is_even = lambda num: num % 2 == 0
    print(is_even(10)) # Calls and uses Lambda expression to check if a number is even.
    
    # TODO: Lambda function to find the max of two inputted values:
    max_value = lambda x, y: x if x > y else y
    print(max_value(5, 10)) # Calls and uses Lambda expression to find the max of two values.
    
    # Dealing with Default Arguments:
    print((lambda a,b,c=0: (a+b+c)/c if c != 0 else (a*b))(2,5,6))
    print((lambda a,b,c=0: (a+b+c)/c if c != 0 else (a*b))(2,5))
    
    # Dealing with Variable Length Arguments:
    print((lambda *args: sum(args))(2,5,6,8,9,10))
    print((lambda *args: sum(args))(2,5,6))
    
    # Dealing with Keyword Arguments:
    print((lambda **kwargs: sum(kwargs.values()))(a=2, b=5, c=6))
    print((lambda **kwargs: sum(kwargs.values()))(a=2, b=5))
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    # Started Talking about Map and Mapping:
    # NOTE: Typical Map syntax = map(function or lambda, iterables)
    
    values = [10,2,8,3,5]
    
    # TODO: Map to go through a list and say if the value is TorF for being >= 5, adds TorF result to a new list:
    print(list(map(lambda x: x >= 5, values)))
    
    print(list(map((lambda x : x ** 3), (5,3,2,1))))
    
    # TODO: Lambda expression to go through 2 sequences of country and capitals and pair the sets:
    countries = ['USA', 'China', 'India', 'Indonesia', 'Canada']
    capitals = ['Washington D.C.', 'Beijing', 'New Delhi', 'Jakarta', 'Ottawa']
    print(list(map(lambda x, y: (x + ' -> ' +  y), countries, capitals)))
    
    # TODO: Lambda expression to the values of a list and tuple at the each matching index:
    list1 = [4, 5, 6, 7]
    tuple1 = (8, 9, 10, 11)
    print(list(map(lambda x, y: (x+y), list1, tuple1)))
