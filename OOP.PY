#creating class
class Employee():
    def ShowIncome(self):
        if self.salary>=100000:
            return "high earning"
        elif (self.salary<100000) & (self.salary>50000):
            return "medium earning"
        else:
            return "low earning"
    #pass
#create object/instance
emp1=Employee()
emp1.name='somali'
emp1.salary=54000
print("name: ",emp1.name,"and salary ",emp1.salary)
print(emp1.ShowIncome())