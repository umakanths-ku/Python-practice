import random 
from wordslists import words

#dictionary of key:()
hangman_art = {0:("  ",
                  "  ", 
                  "  "),
               1:(" o ", 
                  "   ", 
                  "   "), 
               2:(" o ", 
                  " | ", 
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "), 
               4:(" o ",
                  "/|\\",
                  "   "), 
               5:(" o ",
                  "/|\\",
                  "/   "), 
               6:(" o ", 
                  "/|\\",
                  "/ \\")} 

def display_man(wrong_guesses): # will print the ascii art
    for line in hangman_art[wrong_guesses]:
     print(line)
def display_hint(hint): #to display the hint below
    print(" ".join(hint))

def display_answer(answer):# to diplay the answer
    print(" ".join(answer))

def main():
   answer = random.choice(words).lower()#choosing the the random movie name
   hint = ["_"] * len(answer)#will give the no of underscore = no of characters in the movie name
   wrong_guesses = 0   #decides the hangman art to be displayed
   guessed_letters = set()# stores the letters guessed
   is_running = True 
   print("Welcome to hangman game..")
   print("Enter your movie..")
   while is_running: 
       display_man(wrong_guesses)
       display_hint(hint)
       guess = input("Enter a letter: ").lower() 

       if len(guess) != 1 or not guess.isalpha(): 
          print("Invalid input")
          continue 
       
       if guess in guessed_letters: 
          print(f"{guess} is already guessed")
          continue 
       
       guessed_letters.add(guess)

       if guess in answer: 
        for i in range(len(answer)): # if the guessesed letter is in the answer then the letter will replace all the 
         if answer[i] == guess: #      underscore where the letter will  be present.........
            hint[i] = guess    

       else: 
            wrong_guesses+=1   
       
       
       if "_" not in hint: 
          display_man(wrong_guesses)
          display_answer(answer)
          print("YOU WIN!")
          is_running = False
       elif wrong_guesses >= len(hangman_art) - 1: 
          display_man(wrong_guesses)  
          display_answer(answer)
          print("YOU LOSE!")
          is_running = False     

if __name__ == '__main__': 
    main()