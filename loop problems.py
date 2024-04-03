'''flag=False
num=0
while not flag:
    num=int(input("Enter a number: "))
    if num<=0:
        print("Number needs to be more than 0")
        continue
    flag=True
for i in range(1,11):
    res=i*num
    print(f'{i}*{num}={res}')'''


'''num=int(input("Enter a number: "))
res=1
for i in range(1,num+1):
    res*=i
print(f'Factorial of {num} is {res}')'''
    
'''num1=int(input("Enter 1st number: "))    
num2=int(input("Enter 2nd number: "))   
res1=num1**num2
res2=num2**num1    
print(f'1st raised to the 2nd is {res1}, the opposite is {res2}')'''

'''s=[int(x) for x in input("Enter numbers: ").split(',')]
sumE,sumO=0,0
for i in range(len(s)):
    if s[i]%2==0:
        sumE+=s[i]
    else:
        sumO+=s[i]
print(f'Sum of even is {sumE}. Sum of odd is {sumO}')'''


'''flag=False
num=int(input("Enter your number: "))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")'''


'''x=int(input("Enter 1st number: "))    
y=int(input("Enter 2nd number: ")) 
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        nok = i 
print(f'Nok e {nok}')'''

'''posCount=0
negCount=0
zeroCount=0
while True:
    num=int(input("Enter your number: "))
    if num>0:
        posCount+=1
    elif num<0:
        negCount+=1
    else:
        zeroCount+=1
    choice=input("To exit press e, to continue any key: ")
    if choice=="e":
        print('Thank you')
        break
print(f"Positive numbers: {posCount}" )
print(f"Negative numbers: {negCount}" );
print(f"Zero numbers: {zeroCount}" )'''

'''for i in range(1,200):
    temp=i
    d1=temp%10
    temp/=10
    d2=temp%10
    temp/=10
    d3=temp%10
    if (d1**3+d2**3+d3**3)==i:
        print(i)
#Armstrong numbers    '''
    
    

'''num=int(input('Enter number'))
first=0
second=1
print('0 \n1')
for i in range(num-2):
    third=first+second
    print(third)
    first,second=second,third
#fibonacci '''

n=int(input('Enter number'))
for i in range(n):
       print(' '*(n-i) + '*'*(2*i+1))


