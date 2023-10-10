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
         print(f"your {self.bank_name} has been credicted with{amount} aval alnce is {self.balance}")  
    def withdraw(self,amount):
       if self.balance<amount:
           print("insufficient")
       else:
           self.balance-=amount
           print(f"your {self.bank_name}has been debited with{amount} aval bal is {self.balance}")
           
              

             

obj1=Bank()
obj1.create(12234,"neha",45454545,"kodungallur","savings",20000,"sbi")   
obj1.deposit(300) 
obj1.withdraw(500)     
