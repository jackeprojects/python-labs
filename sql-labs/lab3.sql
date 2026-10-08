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