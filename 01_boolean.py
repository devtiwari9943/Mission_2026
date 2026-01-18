# python data structure 

#1 boolean or bool ( True or False)
# example
my_str = "Hello World"
print(my_str.isalnum())#check if all characters in the string are alphanumeric (letters and numbers only)
print(my_str.isalpha())#check if all characters in the string are alphabetic (letters only)
print(my_str.isdecimal())#check if all characters in the string are decimal characters (0-9)
print(my_str.isdigit())#check if all characters in the string are digits (0-9)
print(my_str.islower())#check if all characters in the string are lowercase
print(my_str.isupper())#check if all characters in the string are uppercase
print(my_str.isspace())#check if all characters in the string are whitespace characters (spaces, tabs, newlines)
print(my_str.istitle())#check if the string is in title case (first letter of each word capitalized)
print(my_str.startswith("Hello"))#check if the string starts with the specified substring
print(my_str.endswith("World"))#check if the string ends with the specified substring



#Boolean and logical operators
print("Boolean and logical operators")
print(True and False)
print(True and True)
print(True or False)
print(True or True)
print(not True)
print(not False)
# example
a = 10
b = 5
print(a > b and b < 10) # True and True -> True
print(a > b or b > 10)  # True or False -> True
print(not(a > b))       # not True -> False 
