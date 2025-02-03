class Account:

    def __init__(self, owner, balance=0):

        self.owner = owner

        self.balance = balance

    def dep(self, cnt):

        self.balance += cnt

        return f"Deposit successful! New balance: {self.balance}"

    def wit(self, num):

        if num > self.balance:

            return "Withdrawals may not exceed the available balance."
        
        self.balance -= num

        return f"Withdrawal successful! New balance: {self.balance}"

    def show_balance(self):

        return f"Account balance: {self.balance}"

name = str(input("Write your name: "))

balance = int(input("Write your started balance: "))

acc = Account(name, balance)

print(acc.show_balance())  

depos = int(input("Write a value of deposite: "))

print(acc.dep(depos))

minus = int(input("Write a withdraw: "))

print(acc.wit(minus))

another_minus = int(input("Write an another withdraw: "))

print(acc.wit(another_minus))      