#File:CS112_A1_T2_3_20231182
#Purpose:this game is for fun called subtract a square and its two players game 
#Name:Muhannad salah tamer badawy
#ID:20231182



import random
import math
global loop
loop=1

def player2func(loop):
    while loop==1:
        global num
        player2 = int(input("Player 2 enter number but it must have square root: "))
        while player2 <= num and loop==1:
            if math.sqrt(player2) % 1 == 0 :
                num -= player2
                print(f"Number in the pile is: {num}")
                loop=0
                if num == 0 :
                 print("Player 2 is winner")
                 break
            while math.sqrt(player2) % 1 !=0 :
                print("This number is invalid")
                player2 = int(input("Player 2 enter number but it must have square root: "))
                break



choise = (input("Enter how do you want to set the pile\nA) Random\nB) By your self: "))   #make the user choose whether he wants the number to be random or to enter it manually
quau=1
while True:
    if choise == "a" :
        num = random.randint(5,1000)
        print(f"Number in the pile is: {num}")
        break
    elif choise == "b" :
        
        num = int(input("Please enter number in the pile: "))
        while  math.sqrt(num) % 1 != num:
            print("This number is invalid")
            num = int(input("Please enter number in the pile: "))
            break
        break
    else:
        print("Invalid choose again")
        choise = (input("Enter how do you want to set the pile\nA) Random\nB) By your self: "))
        break
while num !=0 :
    player1 = int(input("Player 1 enter number but it must has square root: "))
    while player1 <= num:
        if math.sqrt(player1) % 1 == 0 :
            num -= player1
            print(f"Number in the pile is: {num}")
            if num == 0 :
             print(" player 1 is winner")
             quau=0
             break
            elif quau != 0:
             player2func(loop)
             break
        else:
            while  math.sqrt(player1) %1 !=0 :
                print("This number is invalid choose again")
                player1 = int(input("Player 1 enter number but it must has square root: "))
                break