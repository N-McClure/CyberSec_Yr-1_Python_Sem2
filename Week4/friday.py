print(" --- Friday, January 31st, 2025 | 0800 - 1000 ---")

# Continuing Tuple Packing and Un-Packing:

if __name__ == "__main__":
    student1 = ('Bob', 101, 'Oakville', 'bob@bobbert.com')
    print(student1)
    
# Tuple Packing:
student2 = 'James', 202, "Hamilton", "james@jj.com"
print(student2)
print(student2[1]) # Prints the value of tuple at specific index

name, sid, campus, email = student2 # Tuple "student2" will be unpacked and assigned it's corrosponding variable.
print(name)
print(sid)
print(campus)
print(email)

(a,b,c) = (100,200,300) # unpacking at both sides of the assignment operator.
print(a)
print(b)
print(c)

# Swapping vlues between variables:
x = 10
y = 20

print(x,y) # Before the swap.

temp = x
x = y
y = temp
 
print(x,y) # after the swap.

# Another way to swap:
p = 5
q = 10
print(p,q) # Before the swap.
(p,q) = (q,p)
print(p,q) # after the swap.

# Unpacking items into interior variables:
places = [('Canada', 'Ottawa'), ('USA', 'Washington')]
for country, capital in places:
    print(f'{country} has its capital city as {capital}')
    
# New Stuff Starts here:

import math
def circleinfo(r):
    a = math.pi * (r**2)
    c = 2 * math.pi * r
    return a, c

def add(x, y):
    return x + y

# Enumerate Items in a Sequence:
subjects = ['math', 'english', 'physics', 'autoshop', 'woodshop','computer science', 'computer engineering']
for i in range(len(subjects)):
    print(i, subjects[i])
    
print("With Enumeration...")
for f in enumerate(subjects):
    print(f[0], f[1])
    
print("With Index...")
for index, f in enumerate(subjects):
    print(index, f)
    
# Un-packing Tuple with return values:
area1, circ1 = circleinfo(5)
print(area1)
print(circ1)

# Un-Packing Tuple argument in calling a function:
print(add(5,3))
v = (7,5)
# print(add(v)) --> Will NOT Work...needs a 2nd argument.
print(add(*v)) # This will work cause it unpacks the tuple "v" first.