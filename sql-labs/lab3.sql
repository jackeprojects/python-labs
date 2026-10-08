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