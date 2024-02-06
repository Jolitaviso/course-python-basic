INSERT INTO customer (first_name, table_num, number_of_persons)
VALUES  ('Ona', 1, 4),
        ('Antanas', 2, 2),
        ('Marija', 3, 3),
        ('Jonas', 4, 6);

INSERT INTO dish (dish_name, ingredient, weight, cost_of_the_meal)
VALUES ('Cezario salotos', 'Ingredients', 200, 10),
       ('Vištienos kepsnys', 'Chicken', 300, 14),
       ('Guliašas', 'Beef', 250, 10),
       ('Jautienos troškinys', 'Beef', 350, 17),
       ('Dienos sriuba', 'Ingredients', 150, 3),
       ('Kiaulienos maltinis', 'Pork', 200, 5);

-- Pavyzdys užsakymams staliuke Nr. 1
INSERT INTO customer_order (dish_id, name, price, table_num)
VALUES  (1, 'Cezario salotos', 10, 1),
        (2, 'Vištienos kepsnys', 14, 1),
        (3, 'Guliašas', 10, 1),
        (4, 'Jautienos troškinys', 17, 1);

INSERT INTO customer_order (dish_id, name, price, table_num)
VALUES  (5, 'Dienos sriuba', 3, 2),
        (6, 'Kiaulienos maltinis', 5, 2);

INSERT INTO customer_order (dish_id, name, price, table_num)
VALUES  (5, 'Dienos sriuba', 3, 3),
        (1, 'Cezario salotos', 10, 3),
        (6, 'Kiaulienos maltinis', 5, 3);

INSERT INTO customer_order (dish_id, name, price, table_num)
VALUES  (1, 'Cezario salotos', 10, 4),
        (2, 'Vištienos kepsnys', 14, 4),
        (3, 'Guliašas', 10, 4),
        (4, 'Jautienos troškinys', 17, 4),
        (5, 'Dienos sriuba', 3, 4),
        (6, 'Kiaulienos maltinis', 5, 4);

INSERT INTO bill (order_time, service_personnel_id, table_num)
VALUES  ('2024-01-31 16:32', 111, 1),
        ('2024-01-31 17:00', 111, 2),
        ('2024-01-31 17:32', 222, 3),
        ('2024-01-31 17:51', 222, 4);
  


SELECT id FROM customer_order WHERE dish_id = 1 AND name = 'Cezario salotos' AND price = 10 AND table_num = 1;

INSERT INTO bill_line (bill_id, order_id, quantity)
VALUES (1, 1, 1),
       (2, 2, 1),
       (3, 3, 1),
       (4, 4, 1),
       (5, 5, 1),
       (6, 6, 1),
       (7, 7, 1),
       (8, 8, 1),
       (9, 9, 1),
       (10, 10, 1),
       (11, 11, 1),
       (12, 12, 1),
       (13, 13, 1),
       (14, 14, 1),
       (15, 15, 1),
       (16, 16, 1);


SELECT * FROM customer;
SELECT * FROM dish;
SELECT * FROM customer_order;
SELECT * FROM bill;
SELECT * FROM bill_line;


SELECT customer.first_name, customer.table_num, customer_order.name, customer_order.price
    FROM customer
    JOIN customer_order ON customer.id = customer_order.table_num
    ORDER BY customer_order.id;

SELECT customer.first_name, customer.table_num, customer_order.name, customer_order.price
FROM customer
JOIN customer_order ON customer.id = customer_order.table_num;

SELECT customer_order.id, customer.first_name, customer_order.name, customer_order.price
FROM customer_order
JOIN customer ON customer.id = customer_order.table_num;

SELECT bill.id, customer.first_name, bill.order_time, bill.service_personnel_id
FROM bill
JOIN customer ON customer.table_num = bill.table_num;

SELECT bill.id, customer.first_name, customer_order.name, customer_order.price
FROM bill
JOIN customer ON customer.table_num = bill.table_num
JOIN customer_order ON customer_order.table_num = customer.id;



SELECT customer.first_name, customer.table_num, customer_order.name, customer_order.price
FROM customer
JOIN customer_order ON customer.table_num = customer_order.table_num
ORDER BY customer_order.id;
