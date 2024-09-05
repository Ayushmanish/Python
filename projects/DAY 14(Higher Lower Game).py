import random
from game_data import data
from art import logo1
from art import vs
from clear import clear
score=0

def compare(A,B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'

def play_game():
    global score #Adding global score inside the play_game() function 
    ahead=True   #allows the function to modify the global score variable rather than 
    count=0      #creating a new local variable called score within the function's scope. 
    while ahead: #This should resolve the UnboundLocalError you encountered.
        A=random.choice(data)
        B=random.choice(data)
        while A['name']==B['name']:
            B=random.choice(data)

        actual=compare(A,B)
        print(logo1)
        if count>0:
            print(f"you are right! Current Score:{score}")
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
        guess=input("Who has more followers? Type 'A' or 'B': ")
        if guess==actual:
            score+=1
            count+=1
        else:
            ahead=False
        clear()

    print(logo1)
    print(f"sorry, that's wrong. Final Score={score}")



play_game()
decision=True
while decision:
    dec=input("want to improve score? Y/N: ")
    if dec=='Y':
        clear()
        play_game()
    else:
        decision=False