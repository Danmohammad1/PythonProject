#ATM abstraction Implementation

from abc import ABC, abstractmethod

class ATM:

    @abstractmethod
    def withdrawlCash(self):
        pass
    @abstractmethod
    def chechBalance(self):
        pass
    @abstractmethod
    def changePin(self):
        pass


class PNB(ATM):

    def __init__(self,name,accNo,Pin,Balance=0):
        self.Name=name
        self.AccountNumber=accNo
        self.__PIN=Pin
        self.__AccountBalance=Balance

    def withdrawlCash(self):
        pin=int(input("Enter your PIN"))
        if self.__PIN==pin:
            cash=int(input("Enter money"))
            self.__AccountBalance-=cash
        else:
            print("You entered the wrong PIN")

    def checkBalance(self):
        pin=int(input("Enter your PIN"))
        if self.__PIN==pin:
            print("your current balance is :",self.__AccountBalance)

    def changePin(self):
        pin=int(input("Enter your PIN"))
        if self.__PIN==pin:
            newPin=int(input("Enter the New PIN"))
            self.__PIN=newPin
        else:
            print("You Enter the Wrong PIN!")

    def DepositMoney(self,cash):
        pin=int(input("Enter the PIN"))
        if self.__PIN==pin:
            self.__AccountBalance+=cash
            print("Cash Deposit Successfuly!")
while True:
    print("1 Create new Account \n2 Check Balance\n3 withdrawl \n4Deposit Balance\n5 Change Your Pin\n6 Exit")
    choice=int(input())
    if choice==1:
        customerName=input("Enter the Custpmer Name")
        AccounNumber=int(input("Enter the Account Number"))
        Pin=int(input("Eter the ATM PIN"))
        obj=PNB(customerName,AccounNumber,Pin)

    elif choice==2:
        obj.checkBalance()

    elif choice==4:
        cash=int(input("Enter the money which you want deposit"))
        obj.DepositMoney(cash)

    elif choice==5:
        obj.changePin()

    elif choice==3:
        obj.withdrawlCash()
        print("Withdrawl Succesfully!")
    elif choice==6:
        exit()
        











































