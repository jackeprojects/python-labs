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