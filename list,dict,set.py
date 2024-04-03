#1.1
"""
list=[int(x) for x in input("Enter list values with comma").split(",")]
sum=0
for i in list:
    sum+=i
print(f"Sum is {sum}")"""

#1.2
"""
list=[int(x) for x in input("Enter list values with comma").split(",")]
max=list[0]
for i in list:
    if i>max:
        max=i
print(f"Max element is {max}")"""

#1.3
"""
def rev(list):
    newList=list[::-1]
    print(newList)
list=[int(x) for x in input("Enter list values with comma: ").split(",")]
rev(list)"""

#2.1
"""
dict={"Ivan":5,"Gosho":6,"Petar":3,"Drago":4}
sum=0
for key,value in dict.items():
    sum+=value
print(f"Avearge mark of the class is {sum/len(dict)}")
"""

#2.2
"""dict1={'elem1':1,'elem2':2, 'elem3':3}
dict2={'10':10,'20':20, '30':30}
dict1.update(dict2)
print(dict1)"""

#2.3
"""
dict1={'elem1':1,'elem2':2, 'elem3':3}
dict1.pop('elem2')
print(dict1)
del dict1['elem3']
print(dict1)"""

#3.1
"""
list=[int(x) for x in input("Enter list values with comma").split(",")]
tup=tuple(list)
sum=0
for i in tup:
    sum+=i
print(f"Sum is {sum}")"""

#3.2
"""tup=(2,3,8,4,5)
if 2 in tup:
    print("Yes")"""

#4.1
"""
set1={2,2,5,8,9}
set2={4,1,3}
set3=set1.union(set2)
print(set3)"""

#4.2
"""
set1={2,2,5,8,9}
set2={5,9}
if set2.issubset(set1):
    print('Yes')
else:
    print('No')"""

#1
"""def triangleArea():
    a=int(input("Enter a"))
    h=int(input("Enter h"))
    s=1/2*a*h
    print(f"The area is {s}")

def rectangleArea():
    a=int(input("Enter a"))
    b=int(input("Enter b"))
    s=a*b
    print(f"The area is {s}")

def circleArea():
    a=int(input("Enter a"))
    s=3.14*a**2
    print(f"The area is {s}")

choise=input("Enter the figure name[triangle - t, rectangle,- r, circle - c]")
ch=choise.lower()
if ch=="t":
    triangleArea()
elif ch=="r":
    rectangleArea()
elif ch=="c":
    circleArea()
else:
    print(f"Invalid input")
"""

#2
"""
def checker(num):
    numStr=list(num)
    #print(numStr)
    flag=True
    for i in range(len(numStr)):
        if numStr[i]!=numStr[len(numStr)-1-i]:
            flag=False
            break
    return flag

num=input("Enter the num: ")
flag=checker(num)
print(f"The number {num} is {flag}")"""

#3
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("You can not divide by 0")
    else:
        return a/b
choice=input("Enter operation: [+,-,*,/] ")
a=int(input("1st number: "))
b=int(input("2nd number: "))
if choice=='+':
    print(f"The result is {add(a,b)}")
elif choice=="-":
    print(f"The result is {sub(a,b)}")
elif choice=="*":
    print(f"The result is {mul(a,b)}")
elif choice=="/":
    print(f"The result is {div(a,b)}")
else:
    print("Invalid input")"""

#4
def func(list,value):
    newList=[]
    for i in range(len(list)):
        if list[i]>value:
            newList.append(0)
        else:
            newList.append(list[i])
    print(newList)
list=[1,2,3,4,5,6,7,8,9]
num=int(input("Enter the num: "))
func(list,num)