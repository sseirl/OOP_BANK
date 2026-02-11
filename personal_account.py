from datetime import datetime

class Transaction:
    def __init__(self, amount, type):
        self.amount = float(amount)
        self.type = type
        self.time = datetime.now()

    def __str__(self):
        return f"{self.type}: ${self.amount} at {self.time}"


class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount, "Deposit"))
        print("Money deposited!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))
            print("Money withdrawn!")
        else:
            print("Not enough balance!")

    def show_balance(self):
        print("Current balance:", self.balance)

    def show_history(self):
        if not self.transactions:
            print("No transactions yet.")
        for t in self.transactions:
            print(t)


acc_number = input("Enter account number: ")
holder_name = input("Enter account holder name: ")

my_account = Account(acc_number, holder_name)

while True:
    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Show History")
    print("5 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        my_account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw(amount)
    elif choice == "3":
        my_account.show_balance()
    elif choice == "4":
        my_account.show_history()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")