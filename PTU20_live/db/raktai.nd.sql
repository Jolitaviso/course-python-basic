-- Sukuriame "Studentai" lentelę
CREATE TABLE Studentai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(50),
  pavarde VARCHAR(50),
  el_pastas VARCHAR(100),
  telefonas VARCHAR(20)
);

-- Sukuriame "Kursai" lentelę
CREATE TABLE Kursai (
  id INTEGER PRIMARY KEY,
  pavadinimas VARCHAR(50),
  aprasymas TEXT
);

-- Sukuriame "StudentuKursai" lentelę, kuri susieja "Studentai" ir "Kursai" lentelės Many-to-Many ryšiu
CREATE TABLE StudentuKursai (
  id INTEGER PRIMARY KEY,
  studento_id INTEGER REFERENCES Studentai(id),
  kurso_id INTEGER REFERENCES Kursai(id)
);

-- Sukuriame "Kategorijos" lentelę
CREATE TABLE Kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas TEXT
);

-- Sukuriame "Prekes" lentelę
CREATE TABLE Prekes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas TEXT,
  aprasymas TEXT,
  kategorijos_id INTEGER REFERENCES Kategorijos(id)
);


-- Sukuriam duomenų bazės schemą
CREATE TABLE vadovai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL
);

CREATE TABLE darbuotojai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  fk_vadovas_id INTEGER REFERENCES vadovai(id)
);



-- Sukuriam duomenų bazės schemą
CREATE TABLE skelbimai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL,
  turinys TEXT NOT NULL
);

CREATE TABLE kategorija (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pavadinimas VARCHAR(255) NOT NULL
);

CREATE TABLE skelbimu_kategorijos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fk_skelbimo_id INTEGER REFERENCES skelbimai(id),
  fk_kategorijos_id INTEGER REFERENCES kategorijos(id)
);

DROP TABLE StudentuKursai;