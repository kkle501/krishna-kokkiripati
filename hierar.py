class Personal:
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def display(self):
        print(self.name,self.phno)
    
class Emp(Personal):
    def __init__(self,name,phno,empid,subject):
        super().__init__(name,phno)
        self.empid=empid
        self.subject=subject
    def display(self):
        super().display()
        print(self.empid,self.subject)
        
class Sport(Personal):
    def __init__(self,name,phno,totalawards):
        super().__init__(name,phno)
        self.TA=totalawards
    def display(self):
        super().display()
        print(self.TA)
    
    
e1=Emp("sudhir","995172211","2935","Python")
e1.display()
s1=Sport("sudhir","995172211",20)
s1.display()
