#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
bill=input("what was the total bill? ")
bill=float(bill)
tip=input("what percentage tip would you like to give? ")
tip=int(tip)
people=input("how many people to spilt the bill? ")
people=int(people)
bill_per_person=bill/people
final_bill_per_person=((tip*bill_per_person)/100)+bill_per_person
print("each person should pay: "+str(round(final_bill_per_person,2)))
