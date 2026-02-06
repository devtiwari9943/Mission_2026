# how to take input from user in python

a= input("enter any value")# a can store any valye , string ,char ,etc
b=int(input("enter any val"))# now this input statement will only accept integer values
# we can pre difinend our input for string, float, int, char etc by the help of above method






# THERE IS A PROBLEM I HAVE TO KNOW IT 

x=(input("enter first number "))
y= (input("enter second number "))
print(x+y)
# if we take x= 2,y=3
#now here is a catch the output we are expecting is 5 but the output will come 23
#because the python takes both of the input as stings

# SO THEIR ARE 2 TYPES OF SOLUTION FOR THIS PROBLEM 
#1 ST TYPE

#we can pre defined the user input like 
#x =int(input("enter any valye "))
#here we have defined the type of data a user can input if the user input the data other than the defined one it will show an error 


#2nd TYPE


#write the same program but change on thing in print statement 

# x=input("enter first number ")
# y= input("enter second number ")
# print(int(x)+int(y))
#now the compiler will take the string type as a integer because we have mention it in print statement 
# but there is a catch if the string is actual a string does not contain any digit (only digit) will give an error 
# because we cant add int and string(1 + dev ) this will show an error