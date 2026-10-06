# Part D, Inherited and subclass-specific behaviour

# 1. Create a base class Employee with name and a method get_information()
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"{self.name} is a {type(self).__name__}"


# 2. Create Developer(Employee) and add a method that only Developer has
class Developer(Employee):
    def start_coding(self):
        return f"{self.name} is now coding!"


# 3. Create another Employee subclass and give it its own sub-class specific method
class CoffeeBringer(Employee):
    def get_coffee(self):
        return f"{self.name} is now bringing coffee!"


# 4. Demonstrate that both subclasses can use inherited behaviour from Employee
developer_1 = Developer("Maya")
coffee_bringer_1 = CoffeeBringer("Jordan")

print(developer_1.get_information())
print(coffee_bringer_1.get_information())


# 5. Demonstrate that an Employee object can't automatically use a method that only exists in one of its subclasses
employee_1 = Employee("Eric")
#print(employee_1.start_coding())  # AttributeError, Employee has no attribute 'start_coding'