def show_balance(balance): 
    print(f"Your balance is ${balance:.2f}")

def deposit(): 
   amount = float(input("Enter an amount to be desposited."))

   if amount<0: 
       print("that's not a valid amount") 
       return 0
   else: 
       return amount    
def withdraw(balance): 
   amount =  float(input("Enter the amount to be withdrawn: ")) 
   if amount>balance: 
           print("Insufficient amount")
   elif amount < 0: 
          print("Not an real amount ")
   else: 
           return amount     

def main(): 
    print("Banking problem") 
    is_running = True
    balance = 0
    while is_running:
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice=input("Enter a choice(1-4): ")

        if choice == '1': 
            show_balance(balance)
        elif choice == '2': 
            balance+=deposit()
        elif choice == '3': 
            balance-=withdraw(balance)
        elif choice == '4': 
            is_running= False
        else: 
            print("Not a valid input") 
        
    print("Thank you! Have a nice day") 
if __name__ == '__main__': 
     main()    
                
