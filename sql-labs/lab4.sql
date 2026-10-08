-- 1. Show every order with customer's first name, last name, and order status
SELECT first_name, last_name, status
FROM customers INNER JOIN orders
ON orders.customer_id = customers.customer_id;

-- 2. Show all orders made by Erik
SELECT first_name, orders.*
FROM customers INNER JOIN orders
ON orders.customer_id = customers.customer_id
WHERE first_name = 'Erik';