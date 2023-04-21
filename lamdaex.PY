#addition of two  numbers
def sum(a,b):
    return a+b
print(sum(2,4))

#or
#we use lamda function--->to make a function without naming them
# also called anonymous function or lamda function
'''lamda x:print(x)'''
show=lambda x:print(x)
show(5)

def show(num):
    print(num)
show(5)

sum=lambda a,b:a+b
print(sum(10,20))


def greater(num1,num2):
    if num1>num2:
        print(num1)
    else:
        print(num2)
greater(10,11)

great=lambda num1,num2:num1 if num1>num2 else num2
print(greater(20,40))

def mult(a,b,c):
    return a*b*c
print(mult(2,3,4))

multi=lambda a,b,c:a*b*c
print(multi(2,3,4))

#map()-->map(function,sequence)
x=[1,2,3,4,5]
def summ(a,b):
    return a+b
print(list(map(summ,x)))#map object at *address*

x=[1,2,3,4,5]
def square(a):
    return a*a
var=list(map(square,x))
print(var)


x=[1,2,3,4,5]
cube=list(map(lambda x:x**3,x))
print(cube)

l1=[1,2,3,4]
l2=[21,23,45,56]
#l3=[22,25,48,60]
add=list(map(lambda a:a+2,l1))
print(add)
add2=list(map(lambda a,b:a+b,l1,l2))
print(add2)


#filter()--->filter(func,seq)
l1=[1,2,3,4,5,6,7,8,9,21]
even=list(filter(lambda x:x%2==0,l1))#returns value
print(even)
even=list(map(lambda x:x%2==0,l1))#returns the evaluation either true of false
print(even)

l3=['abc','xyr','ghsyse','gxvuy','zzzzz']
l3.sort()
print(l3)

l3=['abc','xyr','ghsyse','gxvuy','zzzzz']
l3.sort(key=lambda x:len(x))
print(l3)

#reduce()--->reduce(function,sequence)
from functools import reduce
l1=[1,2,3,4,5,6]
result=reduce(lambda a,b:a+b,l1)
print(result)