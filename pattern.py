'''
Author:Adarsh v
Date:22/11/24
Description:program to construct pattern of (*),using a nested for loop
'''




n=int(input("enter the no"))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*", end=" ")
    print()
print("  ")

for k in range (1,n+1):
    for l in range (k):
        print("*",end=" ")
    print()
print(" ")

for i in range (n,0,-1):
    for j in range (i):
        print("*",end=" ")
    print()
print("  ")


for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()


