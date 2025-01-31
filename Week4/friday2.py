print(" --- Friday, January 31st, 2025 | 0800 - 1000 ---")

# Talking about Sets and Dictionaries:

# List = [8,1,2,3,1,5,1,9]
# Tuple = (4,8,2,1,5,8,9)
# Set = {5,8,9,2}

# Main Differences:
# 1. Sets do not allow duplicate values, while lists and tuples do.
# 2. Sets are unordered collections of unique elements, while lists and tuples are ordered collections of elements.
# 3. Sets use curly braces {} to define, while lists and tuples use square brackets [] to define.

# Creating a Set:
my_list = [1,2,3,4,5,6,7]
my_set = set(my_list) # Way 1
my_set2 = set([3,4,22,5,6,7]) # Way 2
your_set = {90,4,3,22,1,5,6} # Way 3
print(your_set)

print(my_set)
print(my_set2)

# Adding an element to the sets:
my_set.add(10)
print(f'Set after making the addition of 10: {my_set}')

# Printing the length of the sets:
print(f'Length of my_set: {len(my_set)}')
print(f'Length of my_set2: {len(my_set2)}')

# Updating the Set by adding another collection:
my_set.update(my_set2)
print(f'Set 1 after updating with my_set2: {my_set}') # Basicall a UNION operation.
# NOTE: Notice that the duplicates in the 2 sets were not added...due to it being a set.

# Removing an element from the set:
# NOTE: remove() will raise KeyError when the item is not found.
# NOTE: discard() will not raise a KeyError when the iten is not found.

my_set.remove(5)
print(f'Set 1 after removing 5: {my_set}')

my_set.discard(10)
print(f'Set 1 after discarding 10: {my_set}')

# Accessing Set Elements:
for e in my_set:
    print(e)
    
# Clearing a Set:
my_set.clear()
print(f'Set after clearing: {my_set}')

your_set = {90,4,3,22,1,5,6}
print(your_set)

# Set Operations:
setA = set([1,2,3,4])
setB = set([3,4,5,6,7,8])

# Union:
union_set = setA.union(setB) # Can also use: setA | setB
print(f'Union of setA and setB: {union_set}')

# Intersection:
intersection_set = setA.intersection(setB) # Can also use: setA & setB
print(f'Intersection of setA and setB: {intersection_set}')

# Difference:
difference_set = setA.difference(setB) # Can also use: setA - setB
print(f'Difference of setA and setB: {difference_set}')
# NOTE: The difference between setA and setB is the set of elements that are in setA but not in setB.

# Symmetric Difference:
symmetric_difference_set = setA.symmetric_difference(setB) # Can also use: setA ^ setB
print(f'Symmetric Difference of setA and setB: {symmetric_difference_set}')

# Subset Checking:
subset_check = setA.issubset(setB) # Can also use: setA <= setB
print(f'Is setA a subset of setB? {subset_check}')

# Superset Checking:
supe = set([1,2,3,4,5,6,7,8,9,10])
superset_check = setA.issuperset(supe) # Can also use: setA >= supe
print(f'Is setA a superset of supe? {superset_check}')
superset_check = supe.issuperset(setA) # Can also use: supe >= setA
print(f'Is setA a superset of supe? {superset_check}')