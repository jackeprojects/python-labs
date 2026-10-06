DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS reviews;

-- 1. Create table books, with book_id (primary key), title (must have value), author, year (whole number)
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER
);
DROP TABLE books;

-- 2. Add a rule to books so year must be greater than 1400
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