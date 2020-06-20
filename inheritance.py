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
        
