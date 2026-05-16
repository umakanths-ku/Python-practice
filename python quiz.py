questions = ["Who is the biggest CEO in the world?: ", 
             "Who is the father of India?: ", 
             "How do fish breath?: ", 
             "Who can overwrite the desicion made by a court in India?: "]

options = [["a.Elon musk","b.Jeff bezos","c.Bill gates","d.Sundar pichai"],
           ["a.Bhagat Singh","b.Gandhi","c.Sardar vallabai patel","d.Subash Chandra Bose"],
           ["a.Skin","b.Fin","c.Mouth","d.Gills"],
           ["a.Prime minister","b.Lok sabha speaker","c.President","d.Governer"]]
answer=["a","b","d","c"]
guesses = [] 
c=0 
q=0


for question in questions :
     print("-----------")
     print(question)
     for option in options[q]:
        print(option) 

     guess=input("Enter the correct option: ").lower()
     guesses.append(guess)
     if guess == answer[q]: 
            c+=1
            print("CORRECT ANSWER!")
     else: 
            print("INCORRECT ANSWER!")
            print(f"The correct answer is: {answer[q]}")

     q+=1 
    
    
print("----------")
print('RESULT') 
print("----------") 

print("answers:",end=" ")
for ans in answer: 
      print(ans,end=" ") 
print()

print("guesses:",end=" ")
for guess in guesses: 
      print(guess,end=" ")   
print()   

c=int(c/len(questions)*100)
print(f"Your % is {c}%")