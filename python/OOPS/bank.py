class Bank:
    accno:int
    personname:str
    ifsc_code:int
    branch:str
    ac_type:str
    balance:int
    bank_name=str

    def create(self,accno,personname,ifsc_code,branch,ac_type,balance,bank_name):
        self.accno=accno
        self.personname=personname
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.ac_type=ac_type
        self.balance=balance
        self.bank_name=bank_name
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credicted with amount {amount} available balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance") 
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with amount {amount} available balance is {self.balance}")
    def get_balance(self):
        print(f"your available balance is {self.balance}")    
obj1=Bank()
obj1.create(123456,"neha",675849,"kodungallur","savings",5600,"federalbank")
obj1.deposit(3000)
# obj1.withdraw(5000)
# obj1.get_balance()