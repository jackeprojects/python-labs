-- 9. Show which products Anna has bought, show product names only, each once.
SELECT DISTINCT name FROM products
JOIN order_items ON order_items.product_id = products.product_id
JOIN orders ON orders.order_id = order_items.order_id
WHERE orders.customer_id = 1;

-- 10. Correct Erik's email to erik.johansson@example.com
UPDATE customers
SET email = 'erik.johansson@example.com'
WHERE customers.customer_id = 2;

-- 11. Create view customer_overview (customer id, first name, city, number of orders, no email,
-- include customers without any orders
CREATE VIEW customer_overview AS
SELECT customers.customer_id, first_name, city, COUNT(orders.order_id) AS order_count
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id;

-- 12. Webshop wants to add a birth_date column 'just in case'. What would you say?
-- Write in two sentences

-- I would say that the shop doesn't need birth dates to sell products since you should only collect data you're going to use
-- Storing it 'just in case' adds a risk of breaking GDPR, and of getting leaked if database is hacked