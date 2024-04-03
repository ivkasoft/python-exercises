from math import *
def userInput(figure, size1, size2, result):
    if figure=='sq':
        result=size1**2
    elif figure=='c':
        result=math.pi*size1**2
    elif figure=='r':
        result=size1*size2  
    elif figure=='t':
        result=size1*size2*(1/2)  
    print('Area is:', result)

figureType1 = ['sq','c']  
figureType2 = ['t','r']   
valid=False
while valid==False:
    figure=input('Enter the figure [square - sq | circle-c | recangle -r | triangle - t :')
    if figure in figureType2:
        size1=int(input('Enter 1st value: '))
        size2=int(input('Enter 2nd value: '))
    elif figure in figureType1:
        size1=int(input('Enter 1st value: '))
        size2=0
    elif figure not in figureType2 or figureType2:
        print('Invalid input. Please enter again!')
        continue
userInput(figure, size1, size2, 0)