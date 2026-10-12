# Ask the user for a max price and show all products cheaper than that. Use a ? placeholder
import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

while True:
    max_price = input("Enter max price: ")
    if max_price.isdigit():
        max_price = int(max_price)

        cursor.execute("SELECT * FROM products WHERE price < ?", (max_price,))

        print(cursor.fetchall())
        break

conn.close()