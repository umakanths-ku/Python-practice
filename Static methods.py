class Employee:

    def __init__(self,name,position):
        self.name=name
        self.position = position 

    def get_info(self):                       #Instance method
        return f"{self.name} = {self.position}"    
    

    @staticmethod 
    def is_valid_position(position):
        valid_positions = ["Manager","Cook","Janitor","Cashier"] #static class belongs to to the class not to the object..
        return position in valid_positions
    
employee1 = Employee("Kuttu","Manager")
employee2 = Employee("Kalyani","Cook")
employee3 = Employee("Madhav","Cashier")



print(Employee.is_valid_position("Rocket scientist")) 
print(employee1.get_info())  
print(employee2.get_info())   
print(employee3.get_info())    