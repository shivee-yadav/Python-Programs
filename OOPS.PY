#software---->bath tub curve
#inheritance--->to upgrade software
class A:
    #attributes
    #methods
    print("a")
    def __init__(self,name,roll):
        pass

class B:
    #A
    #Battribute
    #methods
    print("b")

#####
class Students:
    pass

student1=Students()#object student1 of class Students
student1.name="harry"
student1.marks=85


print(student1.name)
print(student1.marks)




###############
class Parrot:
    
    # class attribute
    species = "bird"

    # instance attribute
    def _init_(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu._class_.species))
print("Woo is also a {}".format(woo._class_.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))