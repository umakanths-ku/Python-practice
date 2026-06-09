# Exception = a dispurtion to the program

try:
    number = int(input("Enter a number:"))
    print(1/number) 

except ZeroDivisionError:
    print("You cant divide by zero,Idiot")    

except ValueError:
    print("Enter number")

except Exception:
    print("something went wrong")

finally:
    print("Do something son")    
