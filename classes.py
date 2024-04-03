list0=[]
print("Enter values. The stop enter 0 ")
while True:
    a=int(input('Enter value: '))
    if a==0:
        break
    elif a!=0:
        list0.append(a)
print(list0)
list1=[]
list2=[]
for i in range(len(list0)):
    if list0[i]%2==0 and list0[i]%3==0:
        list1.append(list0[i])
    elif list0[i]%2!=0 and list0[i]%7==0:
        list2.append(list0[i])
if list1:
    max=list1[0]
    for i in range(len(list1)):
        if max<list1[i]:
            max=list1[i]
    print(f"Max value of list1 is {max}")
    list1.sort()
    print(f"Sorted list1 is {list1}")
else:
    print("List1 is empty")
if list2:
    sortList2=sorted(list2,reverse=True)
    print(f"Sorted list2 reversed is {sortList2}")
else:
    print("List2 is empty")