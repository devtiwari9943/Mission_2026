# make a calculator for 2 number using user input and print the result of addition, subtraction, multiplication and division
x = int(input("enter first number "))
y = int(input("enter second number "))
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
if y != 0:
    print("Division:", x / y)
else:
    print("Division: Cannot divide by zero")    