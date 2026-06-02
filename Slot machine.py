import random

def spin_row(): 
    symbols = ["🍒", "🔔", "🍉", "🍋", "⭐"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols)) 
    return results    

def print_row(row):
   print("**************")
   print(" ".join(row))
   print("**************")


def get_payout(row,bet): 
    if  row[0] == row[1] == row[2]:  
        if row[0] == "🍒": 
            return bet * 3
        elif row[0] == "🔔": 
            return bet * 4 
        elif row[0] == "🍉": 
            return bet * 5 
        elif row[0] == "🍋":
            return bet * 6
        elif row[0] == "⭐": 
            return bet * 20
    return 0    
        
def main(): 
    balance = 100 

    print("**********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🔔 🍉 🍋 ⭐")
    print("**********************") 

    while balance > 0: 
        print(f"Current balance: ${balance}") 
        bet = input("Place your bet amount: ")

        if not bet.isdigit(): 
            print("Enter a vaild number")                                                           
            continue 

        bet = int(bet)

        if bet > balance: 
            print("Insufficient balance")
            continue

        elif bet <= 0: 
            print("Must be greater than zero")
            continue 
        
        balance -= bet 
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0: 
            print(f"You have won ${payout}")
        else : 
            print("Sorry you have lost this round") 

        balance+=payout       

        play_again = input("Do you want to spin again(Y/N): ").upper()

        if play_again != 'Y': 
            print(f"Game over! Your final balance is ${balance}")
            break

if __name__ == '__main__': 
    main()