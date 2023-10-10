from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def fund_transfer(self):
        pass
    @abstractmethod
    def bal_enq(self):
        pass
    @abstractmethod
    def transaction_history(self):
        pass
class Gpay(Bank):
    # def fund_transfer(self):
    #     print("g.pay")
    def bal_enq(self):
        print("g.pay balance enquiry")
    def transaction_history(self):
        print("g.pay transaction history") 
gp=Gpay()
gp.bal_enq()     
        