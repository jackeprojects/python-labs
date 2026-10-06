-- 1. Show first name, email of all customers
SELECT first_name, email FROM customers;

-- 2. Show all products in the Shoes category
SELECT * FROM products WHERE category = 'Shoes';

-- 3. Which customers live in Uppsala?
SELECT * FROM customers WHERE city = 'Uppsala';

-- 4. Which product costs exactly 199kr?
SELECT * FROM products WHERE price = 199;

-- 5. Show all products sorted by name
SELECT * FROM products ORDER BY name;