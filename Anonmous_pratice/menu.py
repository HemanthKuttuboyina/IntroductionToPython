class Bank:
    def __init__(self):
        self.balance = 0
    def set_deposit(self,amount):
        self.balance+=amount

    def get_balance(self):
        print(f"Balance: {self.balance}")
bank = Bank()
while True:
    options = input("1. Deposit 2. Balance 3. Quit \n Choice: ")
    if options == "1":
        amount = int(input("Amount: "))
        bank.set_deposit(amount)
    elif options == "2":
        bank.get_balance()
    else:
        break