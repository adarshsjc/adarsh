balance_amount=1000
while True:
    print("1.\tCheck balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")

    elif choice== 2:
        deposit_amount =float(input("Enter the amount"))
        balance_amount= balance_amount+deposit_amount
        print(f"The deposit amount ${deposit_amount} and the current balance ${balance_amount} ")
    elif choice==3:

        withdraw_amount = float(input("Enter the withdraw_amount"))
        if withdraw_amount>balance_amount:
            print("Insufficient balance")

        else:
            balance_amount = balance_amount - withdraw_amount
            print(f"The amount withdrawn from the account ${withdraw_amount} and the balance amount ${balance_amount}")

    elif choice == 4:
        break






