-- 1. Add yourself as customer number 11
INSERT INTO customers VALUES (11, 'MyName', 'Test', 'myname.test@example.com', 'Göteborg', '2026-10-07');

-- 2. Add two products in one INSERT
INSERT INTO products VALUES 
(13, 'Scarf', 'Accessories', 229, 15),
(14, 'Gloves', 'Accessories', 199, 20);

-- 3. Customer 7 (Emma) orders 2 Beanies. Make the order and order item
INSERT INTO orders VALUES (16, 7, '2026-10-07', 'new');
INSERT INTO order_items VALUES (16, 10, 2, 179);

-- 4. Try to add an order with item quantity 0. Which rule stops you?
-- INSERT INTO order_items VALUES (16, 10, 0, 179); -- CHECK constraint failed, quantity must be larger than 0

-- 5. Order 12 has been shipped. Change its status
UPDATE orders
SET status = 'shipped'
WHERE order_id = 12;

-- 6. The Water Bottle (product 5) is back in stock, 50 pieces
UPDATE products
SET stock = 50
WHERE product_id = 5;

-- 7. Raise the price of all Accessories by 10%
UPDATE products
SET price = price * 1.10
WHERE category = 'Accessories';

-- 8. Delete the cancelled order. Its items must go first, why?
DELETE FROM order_items
WHERE order_id = 7;
-- I have to delete the order_items first since its order_id key is a FOREIGN KEY and points towards order_id in orders
DELETE FROM orders
WHERE order_id = 7;

-- 9. Revert Changes so data matches the original data
SELECT COUNT(*) FROM orders; -- gives 15

-- 10. Look at this table:
-- student | phone_numbers | course1 | course2 | course3
-- List every problem you can find

-- Multiple numbers in one cell makes the searching one of the numbers unsearchable
-- There are only 3 courses and a student might take a 4th one
-- Students can have the same course in different cells
-- Student1 might have SQL in course1, while Student2 has SQL in course2
-- this means to search for a specific course you have to query all 3 course-columns

-- 11. In order_sheet, which normal form does the products column break and how would you fix it?
CREATE TABLE order_sheet (
  order_no INTEGER,
  customer TEXT,
  email    TEXT,
  city     TEXT,
  products TEXT,
  total    REAL
);
INSERT INTO order_sheet VALUES
(1, 'Anna Lindqvist', 'anna.lindqvist@example.com', 'Uppsala', 'Hoodie Black, Cap Logo x2', 997),
(3, 'Anna Lindqvist', 'anna.lindqvist@example.com', 'Uppsala', 'Socks 3-pack x3', 387),
(4, 'Sara Ahmed', 'sara.ahmed@example.com', 'Goteborg', 'T-shirt White x2, Joggers Grey', 997),
(6, 'Maria Nilsson', 'maria.n@example.com', 'Malmö', 'Hoodie Black, Beanie', 778),
(11, 'Anna Lindqvist', 'anna.l@example.com', 'Uppsala', 'Joggers Grey x2', 998);
-- It breaks 1NF, multiple items are in one cell (products and quantity)
-- To fix this I would create separate tables for orders and products
-- and order_items which has FOREIGN KEYs pointing to the order and products tables

-- 12. A table has:
-- order_id | customer_id | customer_email | order_date
-- Which column is in the wrong place and why?

-- Customer_email breaks 3NF, the table is supposed to describe the order, not the customer
-- If someones order gets deleted, their email also does.
-- Nothing forces you to update an old email address if the customer enters a new one
-- To fix I would move customer_email into customers table