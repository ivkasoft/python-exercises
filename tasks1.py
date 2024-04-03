#Bank account
'''
class Account:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self):
        num=int(input("Deposit amount: "))
        self.balance+=num
    def withdraw(self):
        num=int(input("Withdraw amount: "))
        if num>self.balance:
            print('Insufficient balance!')
        else:
            self.balance-=num
    def balanceCheck(self):
        print(f'Net balance: {self.balance}')

listAccounts=[]
n=int(input('Enter number of accounts: '))
for _ in range(n):
    name=input("Enter name: ")
    balance = float(input("Enter start balance: "))
    a=Account(name,balance)
    listAccounts.append(a)
flag=False
while True:
    if flag:
        break
    choice=input('Choose account [name]')
    for i in range(len(listAccounts)):
        if listAccounts[i].name==choice:
            option=input('D-deposit\nW-withdraw\nB-Balance check\nE-exit ')
            opt=option.lower()
            if opt=="d":
                listAccounts[i].deposit()
            elif opt=="w":
                listAccounts[i].withdraw()
            elif opt=="b":
                listAccounts[i].balanceCheck()
            elif opt=="e":
                flag=True
                break
            else:
                print('Invalid input!')
        '''


#Student
'''
class Student:
    def __init__(self,name,surname,age,speciality):
        self.name=name
        self.surname=surname
        self.age=age
        self.speciality=speciality
    def show(self):
        print(f'{self.name} {self.surname}, {self.age} години, специалност: {self.speciality}')

listStudents=[]
n=int(input('Enter number of students: '))
for _ in range(n):
    name=input("Enter name: ")
    surname=input("Enter surname: ")
    age=int(input("Enter age: "))
    speciality = input("Enter speciality: ")
    a=Student(name,surname,age,speciality)
    listStudents.append(a)
for i in range(len(listStudents)):
    listStudents[i].show()'''


#zadacha 1
'''
num=None
numList=[]
while True:
    n=int(input("Enter size of the list: "))
    if n>5 and n<35:
        num=n
        break
    print('Number must be 15<n<35!')

while num:
    value=int(input("Enter value in the list: "))
    if value>30 and value<300:
        numList.append(value)
        num-=1
    else:
        print('Value must be 30<value<300!')
print(f'The list is {numList}')

count=0
for i in range(len(numList)):
    decimal=numList[i]//10%10
    if decimal%3==0:
        count+=1
print(f'Number of elements that can be divided by 3: {count}')

min=numList[0]
for i in range(len(numList)):
    if numList[i]<min and i%6==4:
        min=numList[i]
print(f'Min element that can be divided by 6 with 4 reminder: {min}')

numList2=[x for x in numList if 10<=x<100 and (x%2==0 or x%3==0)]
print(f'2nd list : {numList2}')
sum=0
count1=0
for i in range(1,len(numList2),2):
    sum+=numList2[i]
    count1+=1
average=sum/count1
print(f'Average of odd index: {average}')

evenlist=[x for x in numList2 if x%2==0]
if evenlist:
    mineven=evenlist[0]
    for i in range(len(evenlist)):
        if mineven>evenlist[i]:
            mineven=evenlist[i]
    numList2.remove(mineven)
else:
    print("There arent even numbers in list2")'''



#zadacha 2

class Employee:
    def __init__(self,i_num,fname,lname,work_experience,education_level,salary,age):
        self.i_num=i_num
        self.fname=fname
        self.lname=lname
        self.work_experience=work_experience
        self.education_level=education_level
        self.salary=salary
        self.age=age
    def display_info(self):
        print(f"Num: {self.i_num}, name: {self.fname} {self.lname}, exp:{self.work_experience}, educ:{self.education_level},salary:{self.salary}, age{self.age}")
    def bonus(self):
        bonus=0
        if self.education_level=='u':
            bonus=self.salary*0.05
        elif self.education_level=='h':
            bonus=self.salary*0.02
        elif self.education_level=='b':
            pass
        bonus+=self.work_experience*0.012

def sort_employee(employees_list):
    sorted_employees = sorted(employees_list, key=lambda x: x.age)
    for i in range(len(sorted_employees)):
        sorted_employees[i].display_info()

def search_by_name(employees_list, fname, lname):
    for i in range(len(employees_list)):
        if fname==employees_list[i].fname and lname==employees_list[i].lname:
            employees_list[i].display_info()
            return
    print('Not found!!!')

def print_by_education_experience(employee_list,education,experience):
    for i in range(len(employees_list)):
        if education==employees_list[i].education_level and experience==employees_list[i].work_experience:
            employees_list[i].display_info()

def remove_employee(employee_list,i_num):
    for i in range(len(employees_list)):
        if i_num==employees_list[i].i_num:
            employees_list.remove(employees_list[i])  
            print("Information deleted!!!")
            return
    print("Wrong i_num!!!")

def add_employee(employee_list,n):
    for i in range(n):
        i_num=int(input("Enter num: "))
        fname=input("Enter first name: ")
        lname=input("Enter last name: ")
        education_level=input("Enter education: ")
        work_experience=int(input("Enter years of experience: "))
        salary=float(input("Enter salary: "))
        age=int(input("Enter age: "))
        e=Employee(i_num,fname,lname,work_experience,education_level,salary,age)
        employees_list.append(e)

n=int(input("Enter number of employees: "))
employees_list=[]

add_employee(employees_list,n)
sort_employee(employees_list)

print("Search by name")
fname=input("Enter first name: ")
lname=input("Enter last name: ")
search_by_name(employees_list, fname, lname)

educ=input("Enter education: ")
exp=input("Enter experience: ")
print_by_education_experience(employees_list,educ,exp)

i_num=int(input("Enter i_num to be deleted"))
remove_employee(employees_list,i_num)
for i in range(len(employees_list)):
    employees_list[i].display_info()
