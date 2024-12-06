print('Set contains 1, 2, or 3 sticks.\nThe player who takes the last stick is the loser.')

person1=input("enter the name:")
person2=input("enter the name:")
stick=16
while stick!=0:
    if stick!=0:
        print(stick)
        choice=int(input(f"{person1},The no of sticks player can take 1,2 or 3:"))
        stick=stick-choice
        player=person1
    if stick!=0:
        print(stick)
        choice = int(input(f"{person2},The no of sticks player can take 1,2 or 3:"))
        stick=stick-choice
        player=person2
if stick==0:
    print(f"{player}, is the loser.")