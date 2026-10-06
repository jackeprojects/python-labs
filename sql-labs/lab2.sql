DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS reviews;

-- 1. Create table books, with book_id (primary key), title (must have value), author, year (whole number)
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER
);

-- 2. Add a rule to books so year must be greater than 1400
DROP TABLE books;

CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER CHECK (year > 1400)
);

-- 3. Add a column isbn to books. It should be TEXT
ALTER TABLE books ADD COLUMN isbn TEXT;

-- 4. Delete the books TABLE
DROP TABLE books;

-- 5. Create table reviews, with review_id, rating (1-5), comment
CREATE TABLE reviews (
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	FOREIGN KEY (product_id) REFERENCES products (product_id)
);

-- 6. Test reviews, try to add a view rating of 6. What happens?
-- INSERT INTO reviews VALUES (1, 1, 6, 'The best'); -- CHECK constraint failed, rating can't be above 5

-- 7. Test reviews, try to add a review for product 50. What happens?
-- INSERT INTO reviews VALUES (50, 50, 2, 'Not the best'); -- FOREIGN KEY constraint failed, there is no product with the id of 50