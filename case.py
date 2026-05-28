def day_of_week(day): 
    match day:
     case "Sunday" | "Saturday": 
      return True
     case "Monday" | "Tuesday" |  "Wednesday" | "Thursday" | "Friday" : 
       return False 
     case _: 
      return "Not valid" 
     
print(day_of_week("Thursday"))     