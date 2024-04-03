#zad1
"""
list1=[]
list2=[]
while True:
    num=int(input("Enter a number. To exit entrer 0 :"))
    if num==0:
        break
    elif num%3==0 and num%2==0 :
        list1.append(num)
    elif num%7==0 and num%2!=0 :
        list2.append(num)

sum=0
for i in range(1,len(list1),2):
    sum+=list1[i]
print(f"Sum of the elements of list1 is {sum}")
print(list2.sort(reverse=True))
if list2:
    min=list2[0]
    max=list2[0]
    for i in range(len(list2)):
        if list2[i]<min:
            min=list2[i]
    for i in range(len(list2)):
        if list2[i]>max:
            max=list2[i]
    result=min*max
    print(f"Result is {result}")
else:
    print("The 2nd list is empty!")"""

#zad2
class Router:
    def __init__(self,proizvodit,kod,edCena,kol):
        self.proizvodit=proizvodit
        self.kod=kod
        self.edCena=edCena
        self.kol=kol
        
class Kolichka(Router):
    def __init__(self):
        self.products=[]
    def addNew(self,product):
        self.products.append(product)
    def fileOutput(self,fileName,delivery=5):
        totalPrice=self.edCena*1.2+delivery
        with open(filename, 'w') as file:
            file.write("Manufacturer\tCode\tUnit Price\tQuantity\n")
            for product in self.products:
                file.write(f"{product.proizvodit}\t{product.kod}\t{product.edCena}\t{product.kol}\n")
router1 = Router("Manufacturer1", "123", 50.0, 2)
router2 = Router("Manufacturer2", "456", 80.0, 1)
router3 = Router("Manufacturer3", "789", 30.0, 4)

kolichka=Kolichka()
kolichka.addNew(router1)
kolichka.addNew(router2)
kolichka.addNew(router3)
kolichka.fileOutput("kolichka.txt")