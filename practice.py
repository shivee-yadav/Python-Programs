#reverse num
for i in range(100,0,-1):
    print(i)

#adding two num
num1= int(input())
num2= int(input())
print(num1+num2)

#printing the smallest num
list1=[10,20,4]
print(min(list1))

#printing current time with timezone
import datetime
import pytz

current_time= datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

print(current_time)

#Euclidean
def gcd(a,b):
    if(a==0):
        return b
    
    
    return gcd(b%a,a)
    
a=36
b=60
print(gcd(a,b))










#legendre
import math

def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def legendre(start,end):
    for i in range(start,end+1):
        lower = math.isqrt(i)
        upper = lower+1
        if prime(lower) or prime(upper):
            print(f"At least one prime number exists between {lower**2} and {upper**2}")
            
start_num=1
end_num=20
legendre(start_num,end_num)
        
        











