# Ask the user for a category and print how many products it has. Use COUNT and fetchone()
import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

category = input("Enter a category: ").title()

cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (category,))
count = cursor.fetchone()[0]

print(f"{category}: {count}")

conn.close()