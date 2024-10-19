'''
Author:Adarsh v
Date:19/10/24
Description:Python program that performs the following tasks:
Create two separate strings:
Concatenate the two strings with a space in between and store the result in a new variable
Print the concatenated string
Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.
'''



First_name=input("Enter your first name:")
Second_name=input("Enter your second name:")
Name=(First_name+ " " +Second_name)
print(Name)

First_name_length=len(First_name)
print(First_name_length)

Extract_firstname=Name[:First_name_length]
print(Extract_firstname)

Extract_lastname=Name[First_name_length+1:]
print(Extract_lastname)


