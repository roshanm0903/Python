class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = int (balance)
        print ("Account Created\n" )

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"{amount} deposited to account\n")
            print(f"New A/C Balance : {self.balance}")

    def withdraw(self,amount):
        if amount>0:
            if self.balance >= amount:
                self.balance += amount
            else:
                print("Insufficient balance")

    def __str__(self):
        return (f"A/C Holder Name : {self.owner} \n" + f"A/C Balance     : {self.balance}")


acct1 = Account("joe",1000)

print(acct1)

acct1.deposit(200)

acct1.withdraw(2000)
# print("cehcek internal variable")
# # print(acct1.balance)