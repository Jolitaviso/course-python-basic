CREATE TABLE dėstytojai (
  dėstytojo_id INTEGER PRIMARY KEY,
  vardas VARCHAR(50),
  pavardė VARCHAR(50),
  skyrius VARCHAR(100),
  el_paštas VARCHAR(50)
);

ALTER TABLE dėstytojai
ADD kabineto_nr INT;

DROP TABLE dėstytojai;