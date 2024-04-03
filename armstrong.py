num=int(input('Enter num: '))
l=list()
dict=dict()
for i in range(1,num+1):
    l.append(i)
print(l)
for i in l:
    dict[i]=l[len(l)-i]
print(dict)