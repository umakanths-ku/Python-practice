class Student: 
    count = 0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name= name
        self.gpa= gpa
        Student.count += 1 
        Student.total_gpa+=gpa

     #instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avg(cls):
        if cls.count == 0:
            return 0 
        else:
            return f"Anrage gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob",3.4)
student2 = Student("Patrick",2.4)
student3 = Student("Kuttu",4.5)



print(Student.get_count())    
print(Student.get_avg())
