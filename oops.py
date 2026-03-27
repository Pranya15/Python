#abstraction

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()



#account creation
class Acc:
    def __init__(self,balance,accno):
        self.balance = balance
        self.accno = accno

        #debit method
    def debit(self,amt):
        self.balance -= amt
        print("Rs.", amt, "was debited")
        print("total balance=", self.get_balance())

        #credit method
    def credit(self,amt):
        self.balance += amt
        print("Rs.",amt,"was credited")
        print("total balance=", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Acc(100000, 12345)
print(acc1.balance)
print(acc1.accno)
acc1.debit(500)
acc1.credit(1000)