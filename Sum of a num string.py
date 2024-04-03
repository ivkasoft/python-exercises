nums=[int(x) for x in input('Enter the numbers: ').split(',')]
result=0
for i in nums:
    result=result+i
print('The sum is:', result)