number=7777
if number % 2 == 0 or number < 0 or number % 10 ==0: 
    print("False")
else:
    og_num=number
    rev_num=0 
    while number != 0: 
        r=number%10 
        rev_num=(rev_num*10)+r 
        number=int(number/10) 

    if og_num==rev_num: 
        print("True") 
    else: 
        print("False")    