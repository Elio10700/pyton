# rock and paper game

import random

list1 = ['rock','paper','scissors']
while True:
    comp = random.choice(list1)
    user = input("enter rock paper or scissors").lower()
    if comp == user:
        print("it is a tie🤣")
        print(comp)
    elif (user =='rock'and comp == 'scissors') or (user =='paper' and comp == 'rock') or (user == 'scissors' and comp =='paper'):
        print('user wins')
        print(comp)
    else:
        print("computer wins the round")
        print(comp)
    ch = input("do you want  to play again (y/n)").lower()
    if ch == 'n':
        break  
