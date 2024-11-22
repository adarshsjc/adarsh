'''
Author:Adarsh v
Date:22/11/24
Description:a project using list 
'''




list1=[1,87,38,5]

list2=[6,75,66]
list3=list1+list2
even=[]
odd=[]
for i in list3:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print("list 1 is:",list1)
print("list 2 is:",list2)

print("The odd numbers are :",odd)
print("The even numbers are:",even)
list4=even+odd
print("The merged list is:",list4)