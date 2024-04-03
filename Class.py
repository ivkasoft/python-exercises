class Customer:
    bankName="IN Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposite(self):
        #
        amount=eval(input('Enter the amount'))
        self.balance+=amount
        print(f"{self.name} Net amount: {self.balance}")
    def withdraw(self):
        #
        amount=eval(input('Enter the amount'))
        if amount>self.balance:
            print(f"Not enough balance!")
        else:
            self.balance=self.balance-amount
            print(f"The withdraw of {amount} was successful.\nRemaining balance: {self.balance}")
    
print(f"Hello! Welcome to {Customer.bankName}")
name=input("Enter name:")
c1=Customer(name)
while True:
    print("Deposite - D\nWithdraw - W\nExit - E")
    choise=input("Enter option:")
    option=choise.lower()
    if option=="d":
        #amount=eval(input('Enter the amount'))
        #c1.deposite(amount)
        c1.deposite()
    elif option=="w":
        #amount=eval(input('Enter the amount'))
        #c1.withdraw(amount)
        c1.withdraw()
    elif option=="e":
        print("Thank you!")
        break
    else:
        print("Incorect Input! Please enter again!")
        continue