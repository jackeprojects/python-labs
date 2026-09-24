# Part E, __str__

# 1. Create a Product class with name and price
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):  # Task 3: Description for object
        return f"{self.name} costs {self.price}"


# 2. Create one Product object and print it before defining __str__, observe the result
product_1 = Product("Fan", 199)
print(product_1)  # before __str__ method was added, output was: <__main__.Product object at 0x000001A7293F8590>


# 3. Add __str__ so printing the Product gives a useful human-readable description
# See Product class above, __str__() method returns description of the object as a str


# 4. Create 3 Product objects and print them
product_2 = Product("Pen", 1)
product_3 = Product("Notepad", 20)
product_4 = Product("Eraser", 2)
print(product_2)
print(product_3)
print(product_4)


# 5. Use str() on one Product object, store the result in a variable and print its type
product_1_str = str(product_1)
print(type(product_1_str))