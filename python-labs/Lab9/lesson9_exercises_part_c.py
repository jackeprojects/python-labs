# Part C, Duck typing

# 1. Create 2 unrelated classes, Printer and Screen, do not use inheritence between them
# 2. Give both classes a method called display_status()
class Printer:
    def __init__(self):
        pass

    def display_status(self):
        return f"{type(self).__name__}: On"


class Screen:
    def __init__(self):
        pass

    def display_status(self):
        return f"{type(self).__name__}: On"


# 3. Create objects from both classes and store them in the same list
printer_1 = Printer()
screen_1 = Screen()

devices = [printer_1, screen_1]


# 4. Loop through the list and call display_status() on each object
for device in devices:
    print(device.display_status())


# 5.
# Python only checks if object has display_status() method, on runtime,
# hence why Python is okay with this, even if the classes don't share inheritence