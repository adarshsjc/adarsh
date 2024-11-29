num1=int(input("Enter the number:"))
num2=int(input("Enter the second number:"))
def recursive_addition(num1,num2):
    if num1==0:
        return num2
    elif num2==0:
        return num1
    else:
        return recursive_addition(num1+1,num2-1)

a=recursive_addition(num1,num2)
print("The sum of numbers:", a)