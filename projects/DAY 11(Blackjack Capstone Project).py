import random
from art import logo
from clear import clear

def deal_card():
    """return a random card from the deck."""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(start_cards):
    #now we will check for the blackjack(ace+10) for user and the computer
    #if any one of them have the blackjack then return 0.
    #if user got the blackjack then wins, if comp got then loose
    """take a list of cards and return the score calculated from the code"""

    if sum(start_cards)==21 and len(start_cards)==2:
        return 0
    if sum(start_cards)>21 and 11 in start_cards:
        start_cards.remove(11)
        start_cards.append(1)

    return sum(start_cards)

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
    print(logo)
    user_cards=[]
    comp_cards=[]
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(comp_cards)

        print(f"your cards:{user_cards},current score: {user_score}")
        print(f"computer's first card:{comp_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
            break

        decision=input("do you want to draw another card:y/n ? ")
        if decision=='y':
            user_cards.append(deal_card())
        else:
            is_game_over=True


    #from here the computer starts playing
    while computer_score!=0 and computer_score<17:
        comp_cards.append(deal_card())
        computer_score=sum(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

