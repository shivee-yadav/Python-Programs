#wap to count even terms and odd terms by using high order functions
l1=[1,2,3,4,5,6,7,8,90,99,88,77,66,55,44,33,22,11]
even=len(list(filter(lambda a: a%2==0,l1)))
print(even)
odd=len(list(filter(lambda a: a%2!=0,l1)))
print(odd)

#find intersection of two array list(int elements)
l1=[1,2,3,4,45]
l2=[2,3,45,5,4]
common=list(filter(lambda a:a in l2,l1))
print(common)


#function to replace a character c1 with c2 and c2 with c1 in given string
str1="hello dear how are you?"
c1='e'
c2='a'
replace=list(map(lambda x:x if (x!=c1 and x!=c2) else c1 if x==c2 else c2,str1))
print(''.join(replace))

#program to find number divisible by 13 using anonymous function
l1=[1,2,3,4,5,6,7,8,90,99,88,77,66,55,44,33,22,11]
even=list(filter(lambda a*2: a%2==0,l1))
print(even)
odd=list(filter(lambda a+2: a%2!=0,l1))
print(odd)


