Sure! Here's a README file for the Customer Order Management System:

---

# Customer Order Management System

## Description

The Customer Order Management System is a Python-based application that manages customer data, product information, and order processing. It uses pandas for data manipulation, SQLite for database storage, and Object-Oriented Programming (OOP) for structure. The system includes functionalities for adding customers and products, placing orders, and generating reports.

## Features

- Add new customers to the system.
- Add new products to the system.
- Place orders for customers.
- Generate detailed order reports.
- Use SQLite for persistent data storage.
- Manipulate and analyze data using pandas.

## Prerequisites

- Python 3.x
- pandas library
- sqlite3 library (included in Python standard library)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/customer-order-management-system.git
   cd customer-order-management-system
   ```

2. **Install required packages**:
   ```bash
   pip install pandas
   ```

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Adding customers**:
   ```python
   customer1 = Customer('Qudrat', 'Qudrat@gmail.com')
   customer1.save_to_db()

   customer2 = Customer('Zain', 'Zain@gamail.com')
   customer2.save_to_db()
   ```

3. **Adding products**:
   ```python
   product1 = Product('Laptop', 1000.0)
   product1.save_to_db()

   product2 = Product('Smartphone', 500.0)
   product2.save_to_db()
   ```

4. **Placing orders**:
   ```python
   order1 = Order(1, 1, 2)
   order1.save_to_db()

   order2 = Order(2, 2, 1)
   order2.save_to_db()
   ```

5. **Generating reports**:
   ```python
   oms = OrderManagementSystem()
   customers_df = oms.get_customers()
   products_df = oms.get_products()
   orders_df = oms.get_orders()
   order_report_df = oms.generate_order_report()

   print("Customers:")
   print(customers_df)
   print("\nProducts:")
   print(products_df)
   print("\nOrders:")
   print(orders_df)
   print("\nOrder Report:")
   print(order_report_df)
   ```

## Example

Below is a complete example of how to use the system:

```python
import pandas as pd
import sqlite3
from datetime import datetime

# Set up the SQLite Database
conn = sqlite3.connect('orders.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS customers (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 email TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS products (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 price REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS orders (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 customer_id INTEGER,
                 product_id INTEGER,
                 quantity INTEGER,
                 order_date TEXT,
                 FOREIGN KEY(customer_id) REFERENCES customers(id),
                 FOREIGN KEY(product_id) REFERENCES products(id))''')

conn.commit()

# Define Classes
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self):
        with conn:
            c.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (self.name, self.email))

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_to_db(self):
        with conn:
            c.execute("INSERT INTO products (name, price) VALUES (?, ?)", (self.name, self.price))

class Order:
    def __init__(self, customer_id, product_id, quantity):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_to_db(self):
        with conn:
            c.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)",
                      (self.customer_id, self.product_id, self.quantity, self.order_date))

class OrderManagementSystem:
    @staticmethod
    def get_customers():
        df = pd.read_sql_query("SELECT * FROM customers", conn)
        return df

    @staticmethod
    def get_products():
        df = pd.read_sql_query("SELECT * FROM products", conn)
        return df

    @staticmethod
    def get_orders():
        df = pd.read_sql_query("SELECT * FROM orders", conn)
        return df

    @staticmethod
    def generate_order_report():
        query = '''SELECT customers.name AS customer_name, products.name AS product_name, orders.quantity, orders.order_date
                   FROM orders
                   JOIN customers ON orders.customer_id = customers.id
                   JOIN products ON orders.product_id = products.id'''
        df = pd.read_sql_query(query, conn)
        return df

# Adding customers
customer1 = Customer('Qudrat', 'Qudrat@gmail.com')
customer1.save_to_db()

customer2 = Customer('Zain', 'Zain@gmail.com')
customer2.save_to_db()

# Adding products
product1 = Product('Laptop', 1000.0)
product1.save_to_db()

product2 = Product('Smartphone', 500.0)
product2.save_to_db()

# Placing orders
order1 = Order(1, 1, 2)
order1.save_to_db()

order2 = Order(2, 2, 1)
order2.save_to_db()

# Generating reports
oms = OrderManagementSystem()
customers_df = oms.get_customers()
products_df = oms.get_products()
orders_df = oms.get_orders()
order_report_df = oms.generate_order_report()

print("Customers:")
print(customers_df)
print("\nProducts:")
print(products_df)
print("\nOrders:")
print(orders_df)
print("\nOrder Report:")
print(order_report_df)
```
