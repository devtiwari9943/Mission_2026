# SETS in Python

# A set is an unordered collection of unique items. Sets are mutable, meaning you can add or remove items after creation.

# Creating a set
# Using curly braces
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)
print("Type of my_set:", type(my_set))

# Using the set() constructor
another_set = set([6, 7, 8, 9, 10])
print("Another set:", another_set)

# operations on sets

# 1. Adding elements
my_set.add(6)
print("Set after adding 6:", my_set)
#output: Set after adding 6: {1, 2, 3, 4, 5, 6}

my_set.add(3)  # Adding a duplicate element
print("Set after trying to add duplicate 3:", my_set)# it can not add duplicate elements
#output: Set after trying to add duplicate 3: {1, 2,3, 4, 5, 6}

# 2. Removing elements
my_set.remove(2)
print("Set after removing 2:", my_set)
#output: Set after removing 2: {1, 3, 4, 5, 6}

# 3 indexing and slicing

# Sets do not support indexing or slicing because they are unordered collections.
# Attempting to access an element by index will raise a TypeError.

#4 difference 
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6} 
print("Set A:", set_a)
print("Set B:", set_b)
print("Difference (A - B):", set_a.difference(set_b))
print("Difference (B - A):", set_b.difference(set_a))
#output: Difference (A - B): {1, 2}
#output: Difference (B - A): {5, 6}

#5 difference update (modifies the original set)
set_a.difference_update(set_b)
print("Set A after difference update with B:", set_a)
#output: Set A after difference update with B: {1, 2}

# 6. Union
set_c = {1, 2, 3}
set_d = {3, 4, 5}
union_set = set_c.union(set_d)
print("Union of Set C and Set D:", union_set)
#output: Union of Set C and Set D: {1, 2, 3, 4, 5}

# 7. Intersection
intersection_set = set_c.intersection(set_d)
print("Intersection of Set C and Set D:", intersection_set)
#output: Intersection of Set C and Set D: {3}

# 8. Symmetric Difference (elements in either set but not in both)
symmetric_diff_set = set_c.symmetric_difference(set_d)
print("Symmetric Difference of Set C and Set D:", symmetric_diff_set)
#output: Symmetric Difference of Set C and Set D: {1, 2, 4, 5}

# 9. Checking membership(the particular element is present in the set or not)
print("Is 2 in Set C?", 2 in set_c)
print("Is 5 in Set C?", 5 in set_c)
#output: Is 2 in Set C? True
#output: Is 5 in Set C? False

# 10. Iterating through a set
print("Iterating through Set C:")
for item in set_c:
    print(item)
#output: Iterating through Set C:
#1
#2
#3      

# 11. Set comprehension(creating a set using a comprehension (comprehension is a concise way to create sets))
squared_set = {x**2 for x in range(5)}
print("Set of squares from 0 to 4:", squared_set)
#output: Set of squares from 0 to 4: {0, 1, 4, 9, 16}

# 12. Clearing a set(removing all elements from the set)
squared_set.clear()
print("Set after clearing:", squared_set)
#output: Set after clearing: set()

# 13. Length of a set
print("Length of Set D:", len(set_d))
#output: Length of Set D: 3

# 14. Copying a set
copied_set = set_d.copy()
print("Copied Set D:", copied_set)
#output: Copied Set D: {3, 4, 5}

# 15. Frozen Set (immutable version of a set)
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen Set:", frozen_set)
print("Type of frozen_set:", type(frozen_set))
#output: Frozen Set: frozenset({1, 2, 3, 4, 5})
#output: Type of frozen_set: <class 'frozenset '>

# Note: Since frozensets are immutable, you cannot add or remove elements from them.

# This concludes the overview of sets in Python along with their operations.

