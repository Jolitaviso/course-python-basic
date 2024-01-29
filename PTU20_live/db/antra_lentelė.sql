CREATE TABLE studentai (
  id INTEGER PRIMARY KEY,
  vardas VARCHAR(50),
  pavardė VARCHAR(50),
  studijų_programa VARCHAR(100),
  el_paštas VARCHAR(50)
);

ALTER TABLE studentai
ADD gimimo_data DATE;

ALTER TABLE studentai
ALTER COLUMN studijų_programa TEXT;

DROP TABLE studentai;