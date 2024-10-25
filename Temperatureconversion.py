'''
Author:Adarsh v
Date:25/10/24
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
The user should be able to input a temperature in Celsius or Fahrenheit,
and the program should convert it to the other unit using the formula
'''



Temp=int(input("Enter temperature:"))
Temp_scale=input("Is this in Celsius or Fahrenheit?")

if Temp_scale=="C":
    f=(9/5)*Temp+32
    print(f)
else:
    c=(5/9)*Temp-32
    print(c)






