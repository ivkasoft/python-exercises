num=input('Enter num: ')
l=list(num)
print(l)
dict=dict()
for i in range(len(num)):
    dict[num[i]]=num[len(num)-i-1]
print(dict)