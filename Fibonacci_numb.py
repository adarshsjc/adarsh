def fibonacci_number(num):
    lst=[]
    num1=0
    num2=1
    for i in range (num):
        lst.append(num1)
        num1,num2=num2,num1+num2
    return lst