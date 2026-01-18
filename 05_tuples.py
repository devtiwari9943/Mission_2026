# TUPLES in PYTHON
# A tuple is an ordered, immutable collection of elements.
# Tuples are similar to lists, but they cannot be modified after creation.

# Creating a tuple
my_tuple = (1, 2, 3, "hello", "world")
print("Initial tuple:", my_tuple)
print("Type of my_tuple:", type(my_tuple))
# output: (1, 2, 3, 'hello', 'world')

# operations on tuples

# 1 - Accessing elements
print("First element:", my_tuple[0])  # Accessing element using index
print("Last element:", my_tuple[-1])  # Accessing last element using negative index
# output: First element: 1
# output: Last element: world

# we can even loop through the tuple

for item in my_tuple:
    print(item)
# output: 1
# output: 2
# output: 3
# output: hello
# output: world

# 2 - Slicing tuples (creating a new tuple from an existing one)
sliced_tuple = my_tuple[1:4]  # Slicing from index 1 to index 4 (exclusive)
print("Sliced tuple:", sliced_tuple)
# output: Sliced tuple: (2, 3, 'hello')

# 3 - Concatenating tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
# output: Concatenated tuple: (1, 2, 3, 4)

# Tuples are immutable and do not support modification after creation.