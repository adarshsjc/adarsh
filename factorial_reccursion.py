num1=int(input("Enter the number:"))
def recursive_factorial(num):
        if num==1:
            return 1
        else:
            return num*recursive_factorial(num-1)
a=recursive_factorial(num1)
print("The factorial of the number",num1,"is:",a)