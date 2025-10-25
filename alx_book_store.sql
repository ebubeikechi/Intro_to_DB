CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE authors (author_id INT Primary Key,
author_name VARCHAR(215));

CREATE TABLE books (book_id INT PRIMARY KEY,
title VARCHAR(130),
author_id INT, 
FOREIGN KEY (author_id) REFERENCES authors(author_id),
price DOUBLE,
publication_date DATE);


CREATE TABLE Customers (customer_id int Primary Key,
customer_name VARCHAR(215),
email VARCHAR(215),
address TEXT);

CREATE TABLE Orders(order_id INT Primary Key,
customer_id INT,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
order_date DATE);

CREATE TABLE Order_Details(orderdetailid INT Primary Key,
order_id INT,
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
book_id INT,
FOREIGN KEY (book_id) REFERENCES Books(book_id),
quantity DOUBLE);
