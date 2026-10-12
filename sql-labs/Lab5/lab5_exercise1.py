# 1. Write a script that prints all customers as 'First Last (City)'
import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name, city FROM customers")
for first_name, last_name, city in cursor.fetchall():
    print(f"{first_name} {last_name} ({city})")

conn.close()