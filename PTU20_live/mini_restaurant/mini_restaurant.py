import sqlite3

connector = sqlite3.connect('mini_restaurant.db')
cursor = connector.cursor()

def create_table(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255),
        table_num INTEGER,
        number_of_persons INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_order (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dish_id INTEGER,
        name VARCHAR(255),
        price DECIMAL,
        table_num INTEGER,
        FOREIGN KEY (dish_id) REFERENCES dish(id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bill (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_time DATETIME,
        service_personnel_id INTEGER,
        table_num INTEGER,
        FOREIGN KEY (table_num) REFERENCES customer(table_num)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bill_line (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bill_id INTEGER,
        order_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (bill_id) REFERENCES bill(id),
        FOREIGN KEY (order_id) REFERENCES customer_order(id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dish (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dish_name VARCHAR(255),
        ingredient VARCHAR(255),
        weight DECIMAL,
        cost_of_the_meal DECIMAL,
        FOREIGN KEY (ingredient) REFERENCES processed_products(raw_material_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS raw_material (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        weight DECIMAL,
        prime_price DECIMAL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS processed_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        raw_material_id VARCHAR(255),
        processing_method VARCHAR(255),
        net_weight DECIMAL,
        semi_finished_product_price DECIMAL,
        FOREIGN KEY (raw_material_id) REFERENCES raw_material(id)
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS price_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service DECIMAL,
        communal DECIMAL,
        salary DECIMAL,
        cost_of_the_meal DECIMAL
    );
    ''')
      
connector.commit()

def table_exists(connection, table_name):
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
    result = execute_query(connection, query)
    return bool(result)

def connect_to_database(database_name):
    return sqlite3.connect(database_name)

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def print_result(result):
    for row in result:
        print(row)

def order_summary(connection):
    query = '''
    SELECT customer.first_name, customer.table_num, customer_order.name, customer_order.price
    FROM customer
    JOIN customer_order ON customer.id = customer_order.table_num
    ORDER BY customer_order.id;
    '''
    return execute_query(connection, query)

def bill_summary(connection):
    query = '''
    SELECT bill.id, customer.first_name, customer.last_name, SUM(customer_order.price) AS total_amount
    FROM bill
    JOIN customer ON bill.table_num = customer.table_num
    JOIN customer_order ON bill.id = customer_order.bill_id
    GROUP BY bill.id
    ORDER BY total_amount DESC;
    '''
    return execute_query(connection, query)



if __name__ == "__main__":
    database_name = 'mini_restaurant.db'
    connection = connect_to_database(database_name)

    create_table(connection, cursor)

    tables = ['customer', 'customer_order', 'bill']
    for table in tables:
        if not table_exists(connection, table):
            print(f"Table '{table}' does not exist.")
            exit()

    print("\nOrder Summary:")
    print_result(order_summary(connection))

    print("\nBill Summary:")
    print_result(bill_summary(connection))

    connection.close()
