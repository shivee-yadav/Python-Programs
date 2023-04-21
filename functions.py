def fun1(name):
    """function example"""
    print("hello "+name+" how are you?")
fun1("sonali")#function calling
print(fun1.__doc__)#to display documentation inside the function


def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even_odd(21)


def even_odd(num):
    if num%2==0:
        return print("even")
    else:
         return print("odd")
even_odd(21)

def absolute_val(num):#use *num for multiple value input
    if num>0:
        return num
    else:
        return -num
print(absolute_val(-2))

l1=[12,23,45,67,89]
def sum(var):
    total=0
    for i in var:
        total+=i

    return total
print("sum-->",sum(l1))

#default agrs
def  greet(name,msg="how are you"):
    print(name+msg)

greet("ria","hii")

#arbitrary args
def student(*name):
    print("hello "+name[1]+name[2])
student("a","b","c","d","e")

# ** keyword args
def student1(**name):
    print("hello"+name["fname"]+" "+name["lname"])
student1(fname="ria",mname="kumari",lname="namdeo")


def reverse(name):
     rname=""
     for i in name:
         rname=i+rname
     print(rname)

reverse("sonali")

def rev(name):
    print(name[::-1])
rev("shivee")


def rever(str):
    rev=""
    l=len(str)
    while l>0:
        rev=rev+str[l-1]
        l-=1
    print(rev)

rever("rupesh")

def binsearch(arr,k):#finding leftmost occurence so that array will remain constant
    #arr.append(k);
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]<k:
            l=mid+1
            ans=mid+1
        else:
            r= mid-1
    return ans

arr=[1,2,4,5,6]
print(binsearch(arr,3))







