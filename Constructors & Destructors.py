class BankAccount():
    def __init__(self,account_number,holder_name,account_type,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.account_type=account_type
        self.balance=balance
        print(f"Account created for {self.holder_name}")
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Balance Insufficient")
    def display_details(self):
        print("\n---Account Details ---")
        print("Account Number: ",self.account_number)
        print("Account Holder: ",self.holder_name)
        print("Account Type: ",self.account_type)
        print("Account Balance: ",self.balance)
    def __del__(self):
        print(f"Account object for {self.holder_name} is being deleted")
account1=BankAccount(1211086352,"Sagar Zaveri","Salary Account",1000000)
account1.deposit(10000)
account1.display_details()
account1.withdraw(345000)
account1.display_details()