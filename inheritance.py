#single level
class Person:
    def __init__(self,name,age,mobile) :
         self.name=name
         self.age=age
         self.mobile=mobile

    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("mobile: ",self.mobile)

class Student(Person):
    def __init__(self,name,age,mobile,school,std):
        super().__init__(name,age,mobile)
        self.school=school
        self.std=std
    
    def PrintDetails(self):
        self.display()
        print("school: ",self.school)
        print("class: ",self.std)

raja=Student("raja",20,9999999,"kv",7)
raja.PrintDetails()