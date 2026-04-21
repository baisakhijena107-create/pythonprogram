class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for", self.name)
        print("Initial Balance =", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Updated Balance =", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance =", self.balance)

    def show_balance(self):
        print("Current Balance =", self.balance)


# Create object using constructor
b1 = Bank("Baisakhi", 1000)

# Perform operations
b1.deposit(500)
b1.withdraw(300)
b1.show_balance()