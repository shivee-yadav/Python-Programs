#even from first list and odd from second list
l1=[1,2,3,4,5]
l2=[4,5,6,7,8,9]
l3=[]
i=0

for a in l1:
    if a%2==0:
        l3.append(a)
        i+=1
for b in l2:
    if b%2!=0:
        l3.append(b)
        i+=1
print(l3)


#wap to remove item present at index 3 and add 236 to 4th index and 56.4 at last index
l1.pop(3)
l1.insert(4,236)
l1.append(56.4)
print(l1)


#wap current and previous number
sum=0
pnum=0
for i in range(0,11):
    cnum=i
    sum=cnum +pnum
    print("current number ",cnum,"previous number ",pnum," sum",sum)
    pnum=cnum

#extract each digit and reverse
s=""
num=int(input("enter number"))
while num>0:
    r=num%10
    s=s+" "+str(r)
    num=num//10
print(s)

#income tax
income=int(input("enter your income "))
if income<=10000:
    print("YOUR TAX IS RS. 0")
if income>10000 and income<=20000:
    print("YOUR TAX IS RS. ",10000*0.1)
if income>20000 :
    print("YOUR TAX IS RS. ",(10000*0.1+(income-20000)*0.2))   

#RAJESHWARI--->RSI
s=input("enter name ")
size=len(s)
new=s[0]+s[(size//2)-1]+s[size-1]
print(s,"--->",new)

#SONALI--->NAL
s=input("enter name ")
size=len(s)
new=s[(size//2)-1]+s[(size//2)]+s[(size//2)+1]
print(s,"--->",new)

#count letters,digits,spl characters
s=input("enter string ")
alpha=0
digits=0
splchar =0
for i in s:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digits+=1
    else:
        splchar+=1
print("total letters: ",alpha)
print("total digits: ",digits)
print("total special characters: ",splchar)


#s1=sonali
#s2=namdeosonali
#s1 and s2 balanced: true
s1=input("enter string 1")
s2=input("enter string 2")
temp =True
for i in s1:
    if i in s2:
        continue
    else:
        temp=False
print("s1 and s2 balanced:",temp)


    

    
   
    
