

#this is a  simple menu problem using dictionary 


menu= {"pizza": 3.9, 
       "buregr": 4.9,
       "pretzel": 3.9, 
       "dosa": 2.9, 
       "idli": 1.9} 
cart=[]#for entering the food to be purchased
total=0 #to find the total cost of the food
print(f"{"MENU":^16}")
for key , value in menu.items(): 
    print(f"{key:10}: ${value:.2f}") 


while True: #infinite loop  
    food = input("Enter the food item(q to quit):")
    if food == "q": 
        break 
    elif menu.get(food) is not None: 
        cart.append(food)#input is added to the empty cart

for food in cart: 
    total+=menu.get(food)#returns the value of the food
    print(food, end=" ")     

print()
print(f"Your total is:${total:.2f}")    