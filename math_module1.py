'''
Auther:Adarsh v
Date:18/10/24
Description: Python program that uses functions from the math module to perform the following operations on a number provided by the user:
'''
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("Square root of",number,":",square_root)
Factorial=math.factorial(number)
print("Factorial of ",number,":",Factorial)
Power=math.pow(number,2)
print(number,"raised to power 2",":",Power)
