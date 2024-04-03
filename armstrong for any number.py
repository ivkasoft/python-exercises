list=[]
def arm(num,len):
    if len<0:
        return
    cur=num//(10**len)
    list.append(cur)
    arm(num%(10**len),len-1)

def check(num,len):
    sum=0
    for i in range(len):
        sum+=list[i]**len
    if sum==num:
        print(f'{num} is an Armstrong')
    else:
        print(f'{num} is NOT an Armstrong')
    
num=input('Enter number')
len=len(num)
arm(int(num),len)
list.pop(0)
print(list)
check(int(num),len)