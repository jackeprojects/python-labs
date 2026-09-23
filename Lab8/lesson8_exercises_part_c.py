# Part C, Inheritance fundamentals

# 1. Create a base class Account with owner and balance
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# 2. Create SavingsAccount(Account) with an additional interest_rate attribute
# 3. Use super() so SavingsAccount reuses the initialization from Account
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)  # Task 3: added super()

        self.interest_rate = interest_rate


# 4. Create 2 objects and print their attributes
savings_account_1 = SavingsAccount("John", 100000, 0.9)
savings_account_2 = SavingsAccount("Jane", 1000000000, 0.4)

print(savings_account_1.owner, savings_account_1.balance, savings_account_1.interest_rate, sep=" | ")
print(savings_account_2.owner, savings_account_2.balance, savings_account_2.interest_rate, sep=" | ")


# 5. Write the "is-a" statement that explain why this inheritance relationship makes sense
# A SavingsAccount is an Account, it inherits the attributes, methods and everything inside of __init__ from Account,
# having Account inside of the parenteses of SavingsAccount indicates that its a child of base class Account