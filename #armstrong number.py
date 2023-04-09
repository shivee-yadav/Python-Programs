#armstrong number
num= int(input("enter a number: "))
sum=0
r=0
n1=num
n2=num
count=0
while(num!=0):
    num=num//10
    count+=1
while(n1>0):
    r=n1%10
    sum=sum+ r**count
    n1=n1//10
if sum==n2:
    print(n2,"is an armstrong number")
else:
    print("it's not an armstrong number ")
