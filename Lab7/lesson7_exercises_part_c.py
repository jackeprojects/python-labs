# Part C, Instance and class attributes

# 1. Create a Product class with name and price as instance attributes
# 2. Add a class attribute called tax_rate that is shared by all Product objects
# 3. Add a price_with_tax() method that returns the price including tax
class Product:
    tax_rate = 0.35

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return round(self.price + (self.price * self.tax_rate), 2)


# 4. Create at least three Product objects and print their prices with tax
graphics_card = Product("Nvidia RTX 5090", 9999)
processor = Product("AMD Ryzen 7 9800X3D", 999)
monitor = Product("Samsung Odyssey G9", 2999)

print(graphics_card.price_with_tax())
print(processor.price_with_tax())
print(monitor.price_with_tax())


# 5. Change Product.tax_rate and show how it affects the Product objects
Product.tax_rate = 0.45

print(graphics_card.price_with_tax())
print(processor.price_with_tax())
print(monitor.price_with_tax())
print(Product.tax_rate)


# 6. Give one Product object its own tax_rate, print the tax rate from that object, another Product object,
# and in the product class
graphics_card.tax_rate = 0.15

print(graphics_card.tax_rate)
print(processor.tax_rate)
print(monitor.tax_rate)
print(Product.tax_rate)