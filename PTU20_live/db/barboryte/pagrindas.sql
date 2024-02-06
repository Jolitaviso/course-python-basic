--CREATE TABLE customer 
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

--CREATE TABLE product 
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(18,2) NOT NULL
);

--CREATE TABLE bill 
CREATE TABLE IF NOT EXISTS bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_datetime DATETIME NOT NULL,
    cachier_id INTEGER NOT NULL,
    customer_id INTEGER REFERENCES customer(id)
);

ALTER TABLE bill ADD COLUMN IF NOT EXISTS cashier_id INTEGER NOT NULL;

--DROP TABLE BILL_LINE
CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER REFERENCES bill(id),
    product_id INTEGER REFERENCES product(id),
    quantity DECIMAL(10,2)
);


INSERT INTO product (name, price) VALUES ('Product1', 10.99), ('Product2', 15.99), ('Product3', 20.99);
INSERT INTO customer (first_name, last_name) VALUES ('John', 'Doe'), ('Jane', 'Doe');
INSERT INTO bill (purchase_datetime, cashier_id, customer_id) VALUES ('2022-01-01 10:00:00', 1, 1), ('2022-01-02 11:30:00', 2, 2);
INSERT INTO bill_line (bill_id, product_id, quantity) VALUES (1, 1, 2), (1, 2, 1), (2, 3, 3);