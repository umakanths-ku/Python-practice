class Looks:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled =is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "Not filled"}")    

class Circle(Looks): 
    def __init__(self,color,is_filled,radius): 
        super().__init__(color,is_filled)
        self.radius = radius 
    def describe(self): 
        super().describe()
        print(f"The area of the circle is {3.14 * self.radius * self.radius} cm^2") 
           

class Square(Looks):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled) 
        self.width = width
    def describe(self): 
        super().describe()
        print(f"The area of the square is {self.width * self.width} cm^2")    

        
        
class Triangle(Looks): 
    def __init__(self,color,is_filled,width,height): 
        super().__init__(color,is_filled)
        self.width = width
        self.height = height 

    def describe(self): 
        super().describe()
        print(f"The area of the triangle is {0.5 * self.height* self.width} cm^2")    

circle = Circle(color="red",is_filled=True,radius=5)  
square = Square(color="blue",is_filled=True,width=5)  
triangle = Triangle(color="yellow",is_filled=False,height=2,width=3)    


circle.describe()
square.describe()
triangle.describe()