USE alx_book_store;
SHOW CREATE TABLE books;
-- task_4.sql
-- Displays the full description of the 'books' table
-- without using DESCRIBE or EXPLAIN

SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    COLUMN_KEY,
    EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'books';
 