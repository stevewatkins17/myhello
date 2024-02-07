drop user if exists SW;
drop database if exists MyTestDB;

create database MyTestDB;

use MyTestDB;

CREATE USER 'SW'@'%' IDENTIFIED BY 'MyPassword01';
GRANT ALL PRIVILEGES ON MyTestDB.* TO 'SW'@'%';
FLUSH PRIVILEGES;

-- Create 'customers' table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

-- Insert data into 'customers' table
INSERT INTO customers (customer_id, name, email)
VALUES
    (1, 'Xavier', 'xavier@example.com'),
    (2, 'Jane', 'jane@example.com'),
    (3, 'Jalen', 'jalen@example.com');

-- Create 'orders' table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert data into 'orders' table
INSERT INTO orders (order_id, customer_id, order_date, total_amount)
VALUES
    (101, 1, '2023-01-15', 150.50),
    (102, 2, '2023-01-16', 75.20),
    (103, 3, '2023-01-16', 200.00);

-- Create 'order_details' tableMyTest
CREATE TABLE order_details (
    detail_id INT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insert data into 'order_details' table
INSERT INTO order_details (detail_id, order_id, product_name, quantity, price)
VALUES
    (1001, 101, 'Product A', 2, 30.00),
    (1002, 101, 'Product B', 1, 45.50),
    (1003, 102, 'Product C', 3, 25.00),
    (1004, 103, 'Product D', 1, 200.00);


select * from customers;
select * from orders;
select * from order_details;

select 
    c.NAME
    ,o.order_date
    ,o.total_amount
    ,od.price
    ,od.product_name
    ,od.quantity
from customers c
inner join orders o on c.customer_id = o.customer_id
inner join order_details od on od.order_id = o.order_id;

select 
     o.order_date
    ,sum(o.total_amount)
from customers c
inner join orders o on c.customer_id = o.customer_id
inner join order_details od on od.order_id = o.order_id
group by      
    o.order_date
having sum(o.total_amount) > 300;

