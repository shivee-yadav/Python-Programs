list =[]
for i in range (1,11):
    list.append(i)
print(list)

#for even number b/w 1 to 100
l1 =[]
for i in range(1,101):
    if i%2==0:
        l1.append(i)
print(l1)

#list comprehension-->
l2=[x for x in range(1,11)]
print(l2)#1 to 10

#even in single line
l2=[x for x in range(1,11) if x%2==0]
print(l2)

#odd in single line
l2=[x for x in range(1,11) if x%2!=0]
print(l2)

#cube of even
l2=[x**3 for x in range(1,11) if x%2==0]
print(l2)

#square of even
l2=[x**2 for x in range(1,11) if x%2==0]
print(l2)