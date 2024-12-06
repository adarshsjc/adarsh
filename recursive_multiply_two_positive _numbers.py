def multiply_two__numbers(num1,num2):
    if num1>=0 and num2>=0:
        if num2==1:
            return num1
        else:
            return num1 + multiply_two__numbers(num1,num2-1)

l=int(input("Enter the first number:"))
p=int(input("Entre the second number:"))
a=multiply_two__numbers(l,p)
print("The product of numbers is :",a)
