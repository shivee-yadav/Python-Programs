t1=10,20,30,40
print(len(t1))
t2=([1,2,3,4],)#, is syntax
t3=([1,2,3,4])
print(len(t2))
print(len(t1))
print(type(t1))
print(type(t2))
print(type(t3))

#passing dictionaries to functions
#{key:value.....}
#def f_name(**kwargs)
     #keyword arguments
def dict_func(**kwargs):
    print(kwargs)

def swap(**dict1):
    return{v:k  for k,v in dict1.items()}
rever=swap(a=10,b=20,c=30)
print((rever))

#function to accept a number and return a list of all odd numbere for 1 till number passed
''' generators
yield-- defines a generator function
next--

'''
def odd_no(n):
    #oli=[]
    for x in range(1,n):
        if x%2!=0:
            yield x#oli.append(x)
        #return oli

x = odd_no(10000)


import cProfile
cProfile.run('odd_no(10000)')

import sys
print(sys.getsizeof(x))


def yield_ex():
    print("generator started")
    yield 10
    print("generator started")
    yield 20
    print("generator started")
    yield 30
z=yield_ex()
next(z)