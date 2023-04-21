# hierarchical inheritance

class Details:
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
    
    def showData(self):
        print("Id: ",self.id)
        print("Name: ", self.name)
        print("Gender: ", self.gender)

class Employee(Details): #Inheritance
    def __init__(self ,id,name,gender,company,dept):
        super().__init__(id,name,gender)
        self.company=company
        self.dept=dept
    
    def showEmployee(self):
        self.showData()
        print("Company: ", self.company)
        print("Department: ", self.dept)

class Doctor(Details): #Inheritance
    def __init__(self,id,name,gender,hospital,dept):
        super().__init__(id,name,gender)
        self.hospital=hospital
        self.dept=dept
        
    
    def showEmployee(self):
        self.showData()
        print("Hospital: ", self.hospital)
        print("Department: ", self.dept)

print("Employee Object")
    
e=Employee(1,"Prem Sharma","Male","gmr","excavation")
e.showEmployee()
print("\nDoctor Object")
   
d=Doctor(1, "pankaj", "male", "aiims", "eyes")
d.showEmployee()



#maths & science within science
class Science:
    def __init__(self,phy,chem,eng,cs):
        self.phy=phy
        self.chem=chem
        self.eng=eng
        self.cs=cs
    
    def showData(self):
        print("physics: ",self.phy)
        print("chemistry: ", self.chem)
        print("english: ", self.eng)
        print("computer science:",self.cs)

class Maths(Science): #Inheritance
    def __init__(self ,phy,chem,eng,cs,maths):
        super().__init__(phy,chem,eng,cs)
        self.maths=maths
        
    
    def showmaths(self):
        self.showData()
        print("Maths: ", self.maths)
       

class Bio(Science): #Inheritance
    def __init__(self ,phy,chem,eng,cs,bio):
        super().__init__(phy,chem,eng,cs)
        self.bio=bio
        
    
    def showbio(self):
        self.showData()
        print("Biology: ", self.bio)

m=Maths(23,34,56,78,89)
m.showmaths()
b=Bio(56,78,65,78,65)
b.showbio()
