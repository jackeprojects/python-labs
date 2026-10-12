-- 1. Show every order with customer's first name, last name, and order status
SELECT first_name, last_name, status
FROM customers INNER JOIN orders
ON orders.customer_id = customers.customer_id;

-- 2. Show all orders made by Erik
SELECT first_name, orders.*
FROM customers INNER JOIN orders
ON orders.customer_id = customers.customer_id
WHERE first_name = 'Erik';

-- 3. Show all orders from Göteborg, newest first
SELECT city, orders.*
FROM customers INNER JOIN orders
ON orders.customer_id = customers.customer_id
WHERE city = 'Göteborg'
ORDER BY order_date DESC;

-- 4. Show every order item with the product name and category
SELECT name, category, order_items.*
FROM products INNER JOIN order_items
ON order_items.product_id = products.product_id;

-- 5. Show order_id and product name for orders that contained Shoes
SELECT order_id, name
FROM order_items INNER JOIN products
ON products.product_id = order_items.product_id
WHERE category = 'Shoes';

-- 6. Show the full receipt for order 10, product name, quantity, unit price, and line total
SELECT name, quantity, unit_price, unit_price * quantity AS line_total
FROM products INNER JOIN order_items
ON order_items.product_id = products.product_id
WHERE order_id = 10;

-- 7. Show which customers have bought a Hoodie Black (first name and order date)
SELECT first_name, order_date
FROM customers INNER JOIN orders
ON customers.customer_id = orders.customer_id
INNER JOIN order_items
ON order_items.order_id = orders.order_id
INNER JOIN products
ON order_items.product_id = products.product_id
WHERE name = 'Hoodie Black';

-- 8. Show all customers and their orders. including with no orders
SELECT *
FROM customers LEFT JOIN orders
ON customers.customer_id = orders.customer_id;

-- 9. Which products have never been sold?
SELECT *
FROM products LEFT JOIN order_items
ON products.product_id = order_items.product_id
WHERE order_items.order_id IS NULL;

-- 10. Show customers from Uppsala and every product they bought (first name, product name, quantity)
SELECT first_name, products.name, quantity
FROM products INNER JOIN order_items
ON products.product_id = order_items.product_id
INNER JOIN orders
ON order_items.order_id = orders.order_id
INNER JOIN customers
ON orders.customer_id = customers.customer_id
WHERE city = 'Uppsala';