print(" --- Wednesday, January 29th, 2025 | 1400 - 1600 ---")

# Packing and Un-Packing Demo:

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