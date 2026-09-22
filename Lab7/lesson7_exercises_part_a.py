#Part A, Classes objects

# 1. Create a Book class with title, author, and pages, create four Book objects and print their attributes
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book_1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book_2 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 251)
book_3 = Book("Roadside Picnic", "Arkady & Boris Strugatsky", 245)
book_4 = Book("1984", "George Orwell", 328)
print(f"{book_1.title} by {book_1.author} is {book_1.pages} pages.")
print(f"{book_2.title} by {book_2.author} is {book_2.pages} pages.")
print(f"{book_3.title} by {book_3.author} is {book_3.pages} pages.")
print(f"{book_4.title} by {book_4.author} is {book_4.pages} pages.")


# 2. Create a Laptop class with brand, model, ram_gb, and price, create three objects and change price of one of them
class Laptop:
    def __init__(self, brand, model, price, ram_gb=8):  # Task 4: added default value
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop_1 = Laptop("Apple", "MacBook Air",1299, 16)
laptop_2 = Laptop("Dell", "XPS 16", 1000, 16)
laptop_3 = Laptop("Apple", "MacBook Pro", 1999, 16)
print(laptop_3.price)

laptop_3.price = 2999
print(laptop_3.price)


# 3. Create two objects with the same attribute values, use 'is' to check whether they are the same object
book_5 = Book("Dune", "Frank Herbert", 412)
book_6 = Book("Dune", "Frank Herbert", 412)

print("They are the same" if book_5 is book_6 else "They are NOT the same")


# 4. Add a defualt value to at least one __init__ parameter
# See Laptop class above, parameter ram_gb has a default value of 8


# 5. Crate one object using keyword arguments
book_7 = Book(title="The Hunger Games", author="Suzanne Collins", pages=374)