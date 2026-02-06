#   DICTIONARIES in PYTHON
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# Dictionaries are mutable, meaning they can be changed after their creation.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial dictionary:", my_dict)
print("Type of my_dict:", type(my_dict))
# output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# operations on dictionaries

# 1 - Accessing values
print("Name:", my_dict["name"])  # Accessing value using key
print("Age:", my_dict.get("age"))  # Accessing value using get() method
# output: Alice
# output: 30

# we can even loop through the dictionary

for key in my_dict:
    print(key)
# output: name
# output: age
# output: city

# loop for values
for value in my_dict.values():
    print(value)
# output: Alice
# output: 30
# output: New York


# for both 
for key, value in my_dict.items():# .items() method returns key-value pairs
    print(key, value)
# output: name Alice
# output: age 30
# output: city New York

# 2 - Adding or updating key-value pairs
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating an existing key-value pair
print("Updated dictionary:", my_dict)
# output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# 3 - Removing key-value pairs
del my_dict["city"]  # Removing a key-value pair using del
removed_value = my_dict.pop("email")  # Removing a key-value pair using pop()
print("Removed email:", removed_value)
print("Dictionary after removals:", my_dict)
# output: Removed email: alice@example.com
# output: {'name': 'Alice', 'age': 31}

# 4 - Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary.")
# output: Name exists in the dictionary.    

# 5 - Dictionary methods
keys = my_dict.keys()  # Get all keys
values = my_dict.values()  # Get all values
items = my_dict.items()  # Get all key-value pairs
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
# output: Keys: dict_keys(['name', 'age'])
# output: Values: dict_values(['Alice', 31])
# output: Items: dict_items([('name', 'Alice'), ('age', 31
# output: Items: dict_items([('name', 'Alice'), ('age', 31)])])

# 6 - Clearing a dictionary
my_dict.clear()  # Remove all key-value pairs
print("Cleared dictionary:", my_dict)
# output: Cleared dictionary: {}    

# 7 - Nested dictionaries (dictionaries within dictionaries)
nested_dict = {
    "person1": {
        "name": "Bob",
        "age": 25
    },
    "person2": {
        "name": "Carol",
        "age": 28
    }
}
print("Nested dictionary:", nested_dict)
# output: Nested dictionary: {'person1': {'name': 'Bob', 'age': 25}, 'person2': {'name': 'Carol', 'age': 28}}
print("Person1's name:", nested_dict["person1"]["name"])
# output: Person1's name: Bob

# Dictionaries are powerful data structures in Python that allow for efficient data storage and retrieval using key-value pairs.
# They are widely used in various applications, including data manipulation, configuration settings, and more.

