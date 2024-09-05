MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def transaction(drink):
   global profit
   print("Please insert coins.")
   quarters=int(input("How many quarters?: "))*0.25
   dimes=int(input("How many dimes?: "))*0.1
   nickles=int(input("How many nickles?: "))*0.05
   pennies=int(input("How many pennies?: "))*0.01
   sum=quarters+dimes+nickles+pennies
   if(drink=='espresso'):
      if(sum>=1.5):
         print("transaction successful")
         print(f"Here is ${round(sum-1.5,2)} is your change")
         print(f"Here is your {drink} Enjoy!")
         profit+=1.5
      else:
         print("Sorry that's not enough money. Money refunded.")
   
   elif(drink=='latte'):
      if(sum>=2.5):
         print("transaction successful")
         print(f"Here is ${round(sum-2.5,2)} is your change")
         print(f"Here is your {drink} Enjoy!")
         profit+=2.5
      else:
         print("Sorry that's not enough money. Money refunded.")

   elif(drink=='cappuccino'):
      if(sum>=3.0):
         print("transaction successful")
         print(f"Here is ${round(sum-3.0,2)} is your change")
         print("Here is your espresso Enjoy!")
         profit+=3.0
      else:
         print("Sorry that's not enough money. Money refunded.")


         
def compare(order,ingredients):
   flag=0
   for item in ingredients:
      if ingredients[item] > resources[item]:
         flag=1
         print(f"​Sorry there is not enough {item}.")
   if flag==0:
      transaction(order)
   else:
      return

def beverage(order):
   if(order=='espresso'):
      compare(order,MENU[order]['ingredients'])
   elif(order=='latte'):
      compare(order,MENU[order]['ingredients'])
   else:
      compare(order,MENU[order]['ingredients'])

while True:
    inp=input("what would you like? (espresso/latte/cappuccino)")
    if(inp=='off'):
        break
    if(inp=='report'):
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"money:{profit}")
    elif(inp=='espresso'):
       beverage('espresso')
       resources["water"]-=50
       resources["coffee"]-=18
    elif(inp=='latte'):
       beverage('latte')
       resources["water"]-=200
       resources["coffee"]-=24
       resources["milk"]-=150
    elif(inp=='cappuccino'):
       beverage('cappuccino')
       resources["water"]-=250
       resources["coffee"]-=24
       resources["milk"]-=100