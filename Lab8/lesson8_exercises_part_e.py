# Part E, super() and shared initialization

# 1. Create a base class Device with brand and year
# 2. Add shared initialization logic inside Device, and an attribute such as is_active = True
class Device:
    def __init__(self, brand, year: int):
        self.brand = brand
        if year < 0:  # 2. Task 2: initialization logic
            raise ValueError("Year can't be negative")
        self.year = year
        self.is_active = True  # 2. Task 2: is_active attribute

#generic_device = Device("brand", -20)  # ValueError

# 3. Create Laptop(Device) with additional attribute ram_gb, use super()
class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)

        if ram_gb < 0:
            raise ValueError("Ram can't be negative")
        self.ram_gb = ram_gb

laptop_1 = Laptop("Asus", 2026, 16)
print(laptop_1.ram_gb)


# 4. Create another Device subclass with its own additional attribute and use super() again
class Blender(Device):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)

        self.color = color

blender_1 = Blender("Ninja", 2024, "Green")
print(blender_1.color)


# 5. Demonstrate that both subclasses recieve the shared initialization logic from Device without duplicating it
#laptop_2 = Laptop("bad laptop", -200, 8)  # ValueError
blender_2 = Blender("bad blender", -200, "Blue")  # ValueError