# Part D, Dictionaries

# 1. Create dictionary for a laptop with brand, model, RAM, storage, price
laptop = {"brand": "Asus", "model": "ROG Strix SCAR 18", "ram": "128GB DDR5-6400", "storage": "8TB Gen 5 NVME.2 SSD", "price": "64490 SEK"}
print(laptop["brand"])
print(laptop["model"])
print(laptop["ram"])
print(laptop["storage"])
print(laptop["price"])


# 2. Update price, add operating_systems key, and remove one key
laptop.update({"price" : "57990 SEK"})
print(laptop["price"])

laptop["operating_system"] = "Windows 11 Pro"
laptop.pop("price")
print(laptop)


# 3. Use get() for an existing and a missing key, compare with direct indexing
print(laptop.get("brand"))
print(laptop.get("price"))
# with direct indexing, if key doesn't exist it will give KeyError
# with get(), if key doesn't exist it will return None


# 4. Print keys, value and items seperately
print(laptop.keys())
print(laptop.values())
print(laptop.items())


# 5. Create a dictionary mapping courses to study hours, calculate total hours
courses_study_hours = {"course 1": 6, "course 2": 8, "course 3": 3, "course 4": 2, "course 5": 7}
print(sum(courses_study_hours.values()))