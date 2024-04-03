my_list = [13, 2, 3, 2, 1, 2, 5, 6, 2]
index=None
min=my_list[0]
for j in range(len(my_list)):
    if my_list[j]<min:
        min=my_list[j]
        index=j
print(f"Min elem's index is {index}")

mylist = [5,6,4,3,9,7,1,2,5]
# Сортирай в обратен ред
mylist.sort(reverse=True)
print(mylist)
prod=mylist[0]*mylist[len(mylist)-1]
print(f'Product is: {prod}')