# Part B, Methods and state

# 1. Extend your Book class with an is_long() method that returns True if the book has more than 300 pages
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

book_1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
print(book_1.is_long())


# 2. Create a BankAccount class with owner and balance, add a deposit() method that changes the balance
# 3. Add a withdraw() method, prevent withdrawal that would make the balance negative by raising a ValueError
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Add the given amount to the account's balance."""
        self.balance += amount
        
    def withdraw(self, amount: float):
        """Subtract the given amount from the account's balance."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount

account_1 = BankAccount("John", 300)
print(account_1.balance)

account_1.deposit(200)
print(account_1.balance)

account_1.withdraw(50)
print(account_1.balance)


# 4. Create a Task class with title and completed=False, add complete() and reopen() methods
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False


# 5. Create 2 objects from one of the classes and show that changing the state of one object doesn't change the other
book_2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1800)
print(book_1.pages)
print(book_2.pages)

book_2.pages = 180
print(book_1.pages)
print(book_2.pages)