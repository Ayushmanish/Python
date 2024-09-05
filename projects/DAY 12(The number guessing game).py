import random
import math

lower=int(input("enter the lower number:"))
upper=int(input("enter the upper number"))

x=random.randint(lower,upper)
y=round(math.log((upper-lower+1),2))
print("\nyou have only ",y,"chances to guess the number")
flag=0
for i in range(y):
 guess=int(input("Guess the number:"))
 if(guess<x):
  print("your guess is low")
  print("only ",(y-(i+1)),"guesses left")
 elif(guess==x):
  print("Congratulations! you did it in ",i+1,"try")
  flag=1
  break
 else:
  print("your guess is high")
  print("only ",(y-(i+1)),"guesses left")

if(flag==0):
 print("you are the loser")
 print("the random no. is:",x)