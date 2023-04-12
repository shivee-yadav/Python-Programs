#
i=20
while(i<=200):
    if(i%2==0):
        print(i)
    i+=1
else:print('over')




#take 10 positive integer input from keyboard using loop and print their sum and average value
i=10
sum=0
while(i>0):
    num = int(input("enter number"))
    if(num>0):
       sum=sum+num
    i-=1
print("sum:",sum)
print("average:",sum/10)



#table of 29
i=1
while(i<=10):
    print(29*i)
    i+=1




#wap to calculate factorial a number given  by user
num= int(input("enter a positive number"))
fact=1
if num==0:
    print("factorial of 0 is 1")
elif num>0:
    n=num
    while(num>0):
        fact=fact*num
        num-=1
    print("factorial of ",n," is ",fact)
else: print("you've a entered negative number")



#count digits of number
num= int(input("enter a  number"))
count=0
while(num!=0):
    num=num//10
    count+=1
print(count)


#sum of digits
num= int(input("enter a  number"))
sum=0
while(num!=0):
    sum=sum + num%10
    num=num//10
print(sum)





    