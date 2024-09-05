#password=[5]
#password[0]="ayush"
#print(type(password))
#print(len(password))
#print(password)
#print("hello world")

# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.color('red')
# timmy.shape('turtle')
# timmy.forward(100)


# myscreen=Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick

from prettytable import PrettyTable
obj=PrettyTable()
obj.field_names=['Student','Marks']
obj.add_rows([
    ['Ayush','89'],
    ['Aditya','88']
])
print(obj)
obj1=PrettyTable()
obj1.add_column('Fruit',['Apple','mango','banana','orange'])
obj1.add_column('Vegetable',['tomato','potato','ladyfinger','brinjal'])
print(obj1)