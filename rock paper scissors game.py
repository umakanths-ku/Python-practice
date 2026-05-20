import random 
options = ("rock","paper","scissors")
a=0
s=0
running = True
while running:
   player=None
   computer=random.choice(options)
   while player not in options :
    player=input("Enter your choice: ").lower()

   print(f"Player: {player}")
   print(f"Computer: {computer}") 

   if player == computer: 
    print("it is a tie!") 
   elif player=="rock" and computer=="scissors":
      print("You win!") 
      a+=1
   elif player=="paper" and computer=="rock":
      print("You win!")
      a+=1
   elif player== "scissors" and computer=="paper":
      print("You win!")
      a+=1
   else : 
      print("You lose!") 
      s+=1
   play_again=input("Do you want to play(y/n): ").lower()
   if not play_again=="y": 
     
     break 


print(f"YOUR SCORE: {a}")
print(f"OPPO SCORE: {s}")
if a==s :
  print("Its a tie..")
elif a>s: 
  print("You win!")
else: 
  print("oppo won")  


print("Thanks for playing..")   
      