import random
from question_model import Question
from data import question_data
from clear import clear


question_bank=[]
for items in question_data:
    new_question=Question(items['text'],items['answer'])
    question_bank.append(new_question)

def play_game():
    score=0
    for i in range(1,6):
        obj=random.choice(question_bank)
        res=input(f"Q.{i}: {obj.text} (True/False)?:" )
        if res.title()==obj.answer:
            print('You got it right!')
            print(f'The correct answer was: {obj.answer}')
            score+=1
            print(f'your current score is: {score}/{i}')
        else:
            print('Thats wrong.')
            print(f'The correct answer was: {obj.answer}')
            print(f'your current score is: {score}/{i}')

play_game()
play=True
while play:
    x=input("want to play again? yes/no: ")
    if x=='yes':
        clear()
        play_game()
    else:
        play=False