'''
Author:Adarsh v
Date:28/10/24
Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
 The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program
'''






while True:
    print("1.\t Convert temperature in Celsius  to Fahrenheit")
    print("2.\t Convert temperature in Fahrenheit to celsius")
    print("3. \t Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:

        cel=float(input("Enter the value:"))
        Fah=(9/5)*cel+32
        print(f"Temperature in fahrenheit is {Fah}°F ")
    elif choice==2:
        fah=float(input("Enter the value:"))
        Cel=5/9*(fah-32)
        print(f"Temperature in celsius is {Cel}°C")
    elif choice==3:
        break

    else:
        print("Invalid choice")











