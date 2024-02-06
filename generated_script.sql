-- Sukurkime lenteles ir įveskime duomenis
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255),
    table_num INTEGER,
    number_of_persons INTEGER
);

-- Įveskime duomenis apie klientus
INSERT INTO customer (first_name, table_num, number_of_persons)
VALUES
    ('Ona', 1, 4),
    ('Antanas', 2, 2),
    ('Marija', 3, 3),
    ('Jonas', 4, 6),
