import sqlite3


def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")


def change_stock(conn):
    product = int(input("Product ID: "))
    stock = int(input("New stock: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (stock, product)
    )
    conn.commit()
    print("Saved!")


def show_receipt(conn):
    order = int(input("Order ID: "))
    cursor = conn.execute(
        """
        SELECT products.name, quantity, unit_price
        FROM products INNER JOIN order_items
        ON products.product_id = order_items.product_id
        WHERE order_items.order_id = ?
        """,
        (order,))
    rows = cursor.fetchall()
    if not rows:
        print("No orders found.")
    else:
        total = 0
        for name, quantity, unit_price in rows:
            product_total = (quantity * unit_price)
            print(f"{quantity}x {name} | {unit_price:.2f} | {product_total:.2f}")
            total += product_total
        print(f"Total: {total:.2f}")
    

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product  4) Change stock  5) Show receipt  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "0":
            break
    conn.close()


main()
