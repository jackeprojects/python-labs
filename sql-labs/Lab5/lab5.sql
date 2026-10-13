-- 9. Show which products Anna has bought, show product names only, each once.
SELECT DISTINCT name FROM products
JOIN order_items ON order_items.product_id = products.product_id
JOIN orders ON orders.order_id = order_items.order_id
WHERE orders.customer_id = 1;

-- 10. Correct Erik's email to erik.johansson@example.com
UPDATE customers
SET email = 'erik.johansson@example.com'
WHERE customers.customer_id = 2;