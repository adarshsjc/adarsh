'''
Author:Adarsh v
Date:25/10/24
Description:Write a Python program to find the largest of three numbers.
 The program should take three numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers.
'''


number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
number3=int(input("Enter the third number:"))
if number1>number2 and number1>number3:
    print("The greatest number is",number1)
elif number2>number3:
    print("The greatest number is",number2)
else:
    print("the greatest number is",number3)
