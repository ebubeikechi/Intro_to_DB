import mysql.connector
from mysql.connector import Error

def execute_sql_file(host, port, user, password, sql_query):
    """
    Connects to a MySQL database and executes SQL statements from a file.
    """

    db_connection = None
    cursor = None
    
    try:
        print(f"Connecting to MySQL on {host}:{port} ...")
        db_connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )

        if db_connection.is_connected():
            print("✅ Connection successful!")

        cursor = db_connection.cursor()

        # print(f"Reading SQL file: {file_path}")
        # with open(file_path, 'r', encoding='utf-8') as file:
        #     sql_script = file.read()

        database_created = False
        # Split script by semicolon and execute each statement
        for statement in sql_query.split(';'):
            statement = statement.strip()
            if statement:
                print(f"▶ Executing: {statement[:60]}...")
                cursor.execute(statement)
                if not database_created:
                    print("Database 'alx_book_store' created successfully!")
                    database_created = True

        db_connection.commit()
        print("✅ All statements executed successfully!")

    # except FileNotFoundError:
    #     print(f"❌ ERROR: SQL file not found at path: {file_path}")

    except mysql.connector.Error as e:
        print(f"❌ Couldn't connect to database: {e}")
    except Error as err:
        print(f"❌ Database Error: {err}")
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
            print("↩️ Transaction rolled back due to error.")

    except Exception as ex:
        print(f"❌ Unexpected Error: {ex}")

    finally:
        # Close connections
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("🔒 Database connection closed.")


# --- CONFIGURATION ---
DB_CONFIG = {
    'host': '127.0.0.1',         
    'port': 3306,                
    'user': 'ebubeikechi',       
    'password': 'ebubeikechi',  
}

SqlQuery = """CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE if not EXISTS Authors (author_id INT Primary Key,
author_name VARCHAR(215));

CREATE TABLE if not EXISTS Books (book_id INT PRIMARY KEY,
title VARCHAR(130),
author_id INT, 
FOREIGN KEY (author_id) REFERENCES authors(author_id),
price DOUBLE,
publication_date DATE);


CREATE TABLE if not EXISTS Customers (customer_id int Primary Key,
customer_name VARCHAR(215),
email VARCHAR(215),
address TEXT);

CREATE TABLE if not EXISTS Orders(order_id INT Primary Key,
customer_id INT,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
order_date DATE);

CREATE TABLE if not EXISTS Order_Details(orderdetailid INT Primary Key,
order_id INT,
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
book_id INT,
FOREIGN KEY (book_id) REFERENCES Books(book_id),
quantity DOUBLE);
"""

# --- EXECUTION ---
if __name__ == "__main__":
    execute_sql_file(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        sql_query=SqlQuery
    )
