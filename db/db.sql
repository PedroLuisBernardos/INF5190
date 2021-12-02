CREATE TABLE glissade (
    nom VARCHAR(255) PRIMARY KEY,
    ouvert INTEGER,
    deblaye INTEGER,
    condition VARCHAR(255),
    nom_arr VARCHAR(255),
    FOREIGN KEY (nom_arr) REFERENCES arrondissement(nom_arr)
);

CREATE TABLE arrondissement (
    nom_arr VARCHAR(255) PRIMARY KEY,
    cle VARCHAR(5),
    date_maj TEXT
);

CREATE TABLE patinoire (
    nom_arr VARCHAR(255) PRIMARY KEY,
    nom_pat VARCHAR(255)
);

CREATE TABLE condition (
    date_heure VARCHAR(14),
    ouvert INTEGER,
    deblaye INTEGER,
    arrose INTEGER,
    resurface INTEGER,
    nom_pat VARCHAR(255),
    FOREIGN KEY (nom_pat) REFERENCES patinoire(nom_pat)
    PRIMARY KEY (date_heure, nom_pat)
);

CREATE TABLE piscine (
    id_uev INTEGER,
    style VARCHAR(255),
    nom VARCHAR(255),
    arrondisse VARCHAR(255),
    adresse TEXT,
    propriete TEXT,
    gestion TEXT,
    point_x VARCHAR(20),
    point_y VARCHAR(20),
    equipeme TEXT,
    longitude REAL,
    latitude REAL,
    PRIMARY KEY (style, nom)
);