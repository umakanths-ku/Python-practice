#OBJECTIVE
#Is it at least 8 characters long? 
#Does it contain at least one number (0-9)?
#Does it contain at least one special character(@ # $ % *)
# meets all 3 print password is strong , 2==> moderate , 1 or 0 ==> weak
def check_password_strength(password):
    c=len(password) 
    if c < 8 : 
        return "Weak" 
    else : 
        f=False
        for x in password: 
            if x.isdigit(): 
                f=True 
        a=False   
        if "@" in password or "#" in password or "$" in password or "%" in password or "*" in password : 
            a=True 
        
    if f==True and a==False : 
         return "Moderate" 
    elif f==True and a==True : 
           return "Strong"    
    else: 
         return "Weak"    
         
print(check_password_strength("Qwerty"))      # Expected: "Weak" (Only length < 8, no numbers, no special)
print(check_password_strength("Python2026"))  # Expected: "Moderate" (Length >= 8, has number, but no special)
print(check_password_strength("Secr3t@pass")) # Expected: "Strong" (Meets all 3 criteria)