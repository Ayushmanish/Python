# from replit import clear
#you can call clear() to clear the output in the console.

bids={}
num=[]
any='yes'
while any=='yes':
    name=input("what is your name?")
    price=input("what is your bid? $")
    bids[name]=price
    any=input("are there any other person to bid:yes/no?:")

for item in bids:
    num.append(bids[item])

max_num=max(num)
for item in bids:
    if(bids[item]==max_num):
        break
print(f"the person to bid highest is {item} with biding amount {max_num}")