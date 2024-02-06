
-- Sukurkime lenteles
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255),
    table_num INTEGER,
    number_of_persons INTEGER
);
--DROP TABLE IF EXISTS customer_order;

CREATE TABLE IF NOT EXISTS customer_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER,
    name VARCHAR(255),
    price DECIMAL,
    table_num INTEGER,
    FOREIGN KEY (dish_id) REFERENCES dish(id)
);

--DROP TABLE IF EXISTS bill;

CREATE TABLE IF NOT EXISTS bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_time DATETIME,
    service_personnel_id INTEGER,
    table_num INTEGER,
    FOREIGN KEY (table_num) REFERENCES customer(table_num)
);

CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,
    order_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (bill_id) REFERENCES bill(id),
    FOREIGN KEY (order_id) REFERENCES customer_order(id)
);

--DROP TABLE IF EXISTS dish;
CREATE TABLE IF NOT EXISTS dish (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name VARCHAR(255),
    ingredient VARCHAR(255),
    weight DECIMAL,
    cost_of_the_meal DECIMAL,
    FOREIGN KEY (ingredient) REFERENCES processed_products(raw_material_id)
);

CREATE TABLE IF NOT EXISTS raw_material (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    weight DECIMAL,
    prime_price DECIMAL
);

--DROP TABLE IF EXISTS processed_products;

CREATE TABLE IF NOT EXISTS processed_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_material_id VARCHAR(255),
    processing_method VARCHAR(255),
    net_weight DECIMAL,
    semi_finished_product_price DECIMAL,
    FOREIGN KEY (raw_material_id) REFERENCES raw_material(id)
);

CREATE TABLE IF NOT EXISTS price_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service DECIMAL,
    communal DECIMAL,
    salary DECIMAL,
    cost_of_the_meal DECIMAL
);
