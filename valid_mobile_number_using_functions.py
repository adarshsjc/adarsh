from operator import truediv
from pickle import FALSE


def is_valid_number(number):
    if len(number)==10 and number[0] in "987":
        return True
    return False
mobile_number=input("Enter the mobile number:")
if is_valid_number(mobile_number):
    print(f"THe mobile number is  valid" ,mobile_number)
else:
    print(f"THe mobile number is invalid ",mobile_number)


