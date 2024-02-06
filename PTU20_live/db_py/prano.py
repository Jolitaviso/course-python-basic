import sqlite3

# Patikrinimas ar lentelės egzistuoja
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

def most_sold_products(connection):
    query = '''
    SELECT product.name, SUM(bill_line.quantity) AS total_sold
    FROM product
    JOIN bill_line ON product.id = bill_line.product_id
    GROUP BY product.id
    ORDER BY total_sold DESC
    LIMIT 1;
    '''
    return execute_query(connection, query)

def max_product_revenue(connection):
    query = '''
    SELECT product.name, SUM(product.price * bill_line.quantity) AS total_revenue
    FROM product
    JOIN bill_line ON product.id = bill_line.product_id
    GROUP BY product.id
    ORDER BY total_revenue DESC
    LIMIT 1;
    '''
    return execute_query(connection, query)

def best_customer(connection):
    query = '''
    SELECT customer.first_name, customer.last_name, SUM(product.price * bill_line.quantity) AS total_spent
    FROM customer
    JOIN bill ON customer.id = bill.customer_id
    JOIN bill_line ON bill.id = bill_line.bill_id
    JOIN product ON bill_line.product_id = product.id
    GROUP BY customer.id
    ORDER BY total_spent DESC
    LIMIT 1;
    '''
    return execute_query(connection, query)

def max_bill(connection):
    query = '''
    SELECT bill.id, customer.first_name, customer.last_name,
           SUM(product.price * bill_line.quantity) AS total_amount
    FROM bill
    JOIN customer ON bill.customer_id = customer.id
    JOIN bill_line ON bill.id = bill_line.bill_id
    JOIN product ON bill_line.product_id = product.id
    GROUP BY bill.id
    ORDER BY total_amount DESC
    LIMIT 1;
    '''
    return execute_query(connection, query)

if __name__ == "__main__":
    database_name = 'shop.db'
    connection = connect_to_database(database_name)

    # Užklausų vykdymas ir rezultatų spausdinimas
    tables = ['product', 'customer', 'bill', 'bill_line']
    for table in tables:
        if not table_exists(connection, table):
            print(f"Table '{table}' does not exist.")
            exit()

    print("\nMost Sold Products:")
    print_result(most_sold_products(connection))

    print("\nMax Product Revenue:")
    print_result(max_product_revenue(connection))

    print("\nBest Customer:")
    print_result(best_customer(connection))

    print("\nMax Bill:")
    print_result(max_bill(connection))

    connection.close()
