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

-- 6. Show all customers, the one who joined first at the top
SELECT * FROM customers ORDER BY joined_date;

-- 7. Which products are sold out?
SELECT * FROM products WHERE stock = 0;

-- 8. Show the 3 newest customers
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

-- 9. Show customers from Stockholm or Göteborg. Use IN
SELECT * FROM customers
WHERE city IN ('Stockholm', 'Göteborg');

-- 10. Show product name and price, call columns product and price_sek
SELECT name AS product, price AS price_sek FROM products;