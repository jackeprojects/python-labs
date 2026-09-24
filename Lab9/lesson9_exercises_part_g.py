# Part G, Inheritance or composition

# 1. Create CPU with a model attribute
class CPU:
    def __init__(self, model):
        self.model = model

# 2. Create Computer with brand and a CPU object, use composition, not inheritance
class Computer:
    def __init__(self, brand, cpu: CPU):
        self.brand = brand
        self.cpu = cpu


# 3. Create a CPU object and pass it to a Computer object
cpu_1 = CPU("AMD Ryzen 7 9800X3D")
computer_1 = Computer("Lenovo", cpu_1)


# 4. Print the computer brand and CPU model through the Computer object
print(f"This {computer_1.brand} computer comes with a {computer_1.cpu.model}")


# 5. In comments, explain why "Computer HAS-A CPU" makes more sense than "Computer IS-A CPU"
# Because a CPU is a component of a computer, not the whole computer.
# which is why it's better to pass CPU in as an attribute of Computer, instead of inheriting CPU


# 6. For each pair below, write whether you would most likely use inheritance (IS-A) or composition (HAS-A)
# Car / Engine, Manager / Employee, Course / Teacher, Phone / Device

# Car/Engine - HAS-A, a car HAS an engine
# Manager / Employee - IS-A, a manager is an employee
# Course / Teacher - HAS-A, a course has a teacher that teaches it
# Phone / Device - IS-A, a phone is a type of device