class Book:

    def __init__(self, title , author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.title} {self.author}"
    
    def __eq__(self,other):
        return self.title == other.title and self.author == self.other
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages 
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages+other.num_pages
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"{key} was not found"

        
book1 = Book("Hobbit","J.R.R Tolkein",310)
book2 = Book("GOT","Kuttu",329)
book3 = Book("Scarelletlilly","Umakanth",600) 


print(book2["audio"])



