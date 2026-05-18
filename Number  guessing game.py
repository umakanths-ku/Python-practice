import random 

lowest=1
highest=100
ans=random.randint(lowest,highest)#for creating random number 
guesses= 0 
is_running= True 

print("Python number guessing game")
print(f"Select a number b/w {lowest} and {highest}")

while is_running: #without condition it will be considered as true

    guess=input("Enter your guess: ") 

    if guess.isdigit(): 
        guess=int(guess)
        guesses+=1

 
        if guess < lowest or guess > highest: 
            print("Number is out of range")
            print(f"Select a number b/w {lowest} and {highest}") 
        elif guess < ans:
            print("Too low.. Try again") 
        elif guess > ans: 
            print("Too high.. Try again")
        else: 
            print(f"Correct! The answer was {guess}") 
            print(f"Number of guesses: {guesses}") 
            is_running = False
             

    else: 
        print("invalid")
        print(f"Select a number b/w {lowest} and {highest}")
