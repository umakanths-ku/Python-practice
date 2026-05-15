o=input("Enter an operator (- + * /): ") 
n1=float(input("Enter the first number: "))
n2=float(input("Enter the Second number: ")) 
if o == "-": 
    r=n1-n2 
    print(r) 
elif o == "+": 
    r=n1+n2 
    print(r) 
elif o == "*": 
    r=n1*n2 
    print(r)   
elif o == "/": 
    r=n1/n2 
    print(r) 
else : 
    print("invalid input")
