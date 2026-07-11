# IF STATEMENT

# it means if the condition is true then only the code will be executed otherwise it will not be executed
a= 10
if a > 5:
    print("a is greater than 5")
# output is a is greater than 5     




# ELSE STATEMENT

# it means if the condition is false then only the code will be executed otherwise it will not be executed
b= 3
if b > 5:
    print("b is greater than 5")
else:
    print("b is not greater than 5")
# output is b is not greater than 5



# ELIF STATEMENT
# it means if the first condition is false then it will check the second condition and if the second condition is true then only the code will be executed otherwise it will not be executed
c= 5
if c > 5:
    print("c is greater than 5")
elif c == 5:
    print("c is equal to 5")
else:
    print("c is less than 5")
# output is c is equal to 5



# NESTED CONDITIONALS

# it means if we have to check multiple conditions then we can use nested conditionals
d= 10
if d > 5:
    print("d is greater than 5")
    if d > 8:
        print("d is also greater than 8")
    else:
        print("d is not greater than 8")
else: 
    print("d is not greater than 5")
# output is d is greater than 5
# output is d is also greater than 8