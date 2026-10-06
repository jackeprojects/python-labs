# Part E, Nested collections

# 1. Create a list of at least 5 dictionaries representing books
book1 = {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "pages": 223, "available": False}
book2 = {"title": "1984", "author": "George Orwell", "pages": 328, "available": True}
book3 = {"title": "The Lord of The Rings", "author": "J.R.R. Tolkien", "pages": 1077, "available": True}
book4 = {"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": 310, "available": False}
book5 = {"title": "Moby-Dick", "author": "Herman Melville", "pages": 635, "available": False}

books = [book1, book2, book3, book4, book5]


# 2. Access the title of the third, and the availability of the last book
print(books[2]["title"])
print(books[-1]["available"])


# 3. Change one nested value and add a new key to one book
books[0]["available"] = True
books[0]["genre"] = "fantasy"

print(books[0]["genre"])


# 4. Create a dictionary where each key is a department and each value is a list of employee names
departments = {
    "hr": ["John"],
    "engineering": ["Michael", "Chloe"],
    "sales": ["Sarah", "Kevin"]}


# 5. Create a structure for 3 courses with name, teacher, topics, and print one topic via chained indexing
courses = [
    {"name": "Python Fundementals", "teacher": "Kyle", "topics": ["Variables", "Loops", "Functions"]},
    {"name": "Web Development", "teacher": "Joan", "topics": ["HTML", "CSS"]},
    {"name": "Databases", "teacher" : "Lara", "topics": ["SQL", "Indexing"]}
]

print(courses[1]["topics"][1])