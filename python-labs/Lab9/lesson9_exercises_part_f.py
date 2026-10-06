# Part F, __str__ with inheritance

# 1. Create a base class Account with owner and balance
# 2.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} | {self.balance}"


# 3. Create SavingsAccount(Account) with an additional interest_rate attribute, use super() in __init__
# 4. Override __str__ in SavingsAccount so its output also includes the interest rate
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def __str__(self):
        return f"{super().__str__()} | {self.interest_rate}"


# 5. Create and print both an Account and a SavingsAccount object
account_1 = Account("Jane", 999999)
savings_account_1 = SavingsAccount("John", 10000, 0.25)
print(account_1)
print(savings_account_1)