"""class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        area=self.a*self.b
        print(f"Area is {area}")
    def parameter(self):
        parameter=2*(self.a+self.b)
        print(f"Parameter is {parameter}")
    def __del__(self):
        print("Object is deleted")

a=int(input('Enter a: '))
b=int(input('Enter b: '))
r=Rectangle(a,b)
r.area()
r.parameter()
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f"Hello, i am {self.name} and i am {self.age}")
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def intro(self):
        print(f"Hello, i am {self.name}, i am {self.age} and i am in {self.grade} grade")

n=int(input('Enter number of people:'))
list=[]
for i in range(n):
    name=input("Enter name: ")
    age=int(input('Enter age: '))
    #grade=int(input('Enter grade: '))
    #s=Student(name,age,grade)
    p=Person(name,age)
    list.append(p)
sum=0
for i in range(n):
    print(list[i].age)
for i in range(n):
    sum+=list[i].age
avr=sum/n
print(avr)

"""person=Person(name,age)
person.intro()
student=Student(name,age,grade)
student.intro()"""


