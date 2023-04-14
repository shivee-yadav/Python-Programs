from ast import operator
import sys
print(sys.argv)
print(f'input argv type is:{type(sys.argv)}')
print(f'input argv type is:{len(sys.argv)}')
summ=0
lst=[]
if len(sys.argv[1:]) !=3:
    print("invalid number of args passed")
    print("usage is: sysargv.py arg1 arg2 arg3")
    print("try again!!!")
    sys.exit(0)
operator=''
numlist=[]
for ctr in sys.argv[1:]:
    if ctr.isdigit():
        numlist += [int(ctr)]
    elif ctr in '+-*//':
        operator=ctr

if operator not in '// + - * /'.split():
    print('invalide operator entered\nTry again!!')
    sys.exit()
    
if len(operator)!=1 or operator!='//':
    print("invalid operator entered \nTry Again!!")
    sys.exit()

if len(numlist)!=2:
    print("invalid integers")
    sys.exit()
print('result',eval(numlist[0]+operator+numlist[1]))

for num in sys.argv[1:]:
    if num.isdigit():
        summ +=int(num)
        lst += [int(num)]
else:
    print('Average ---> ',(summ/(len(lst)-1)))
    print('sum ---> ',sum(lst))
    print('max ---> ',max(lst))
    print('min --->',min(lst))
