import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Crée la connection
try:
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("data.db")
    print("Database created")
    con.open()
    print(con.lastError().text())

finally:
    # Si cela ne fonctionne pas, retourne une erreur
    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

# Création des tables si celle-ci n'existe pas dans la BD
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE Personne (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        Prenom VARCHAR(40),
        Nom VARCHAR(40),
        Sexe int,
        cbc int,
        cba int,
        cbe int
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE CartedeCredits (
        id VARCHAR(4),
        NumeroCC int,
        DateCC int,
        CodeCC int,
        FOREIGN KEY (id) REFERENCES Personne(id) ON DELETE CASCADE 
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Client (
    "id" VARCHAR(4),
    "DateInsc" VARCHAR(40),
    "Courriel" VARCHAR(255),
    "ClientPwd" VARCHAR(40),
    FOREIGN KEY("id") REFERENCES "Personne"("id") ON DELETE CASCADE
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Acteurs (
        id VARCHAR(4),
        TitreFilm VARCHAR(40),
        Personnage VARCHAR(40),
        DateDebut VARCHAR(40),
        DateFin VARCHAR(40),
        Cachet VARCHAR(40),
        FOREIGN KEY (id) REFERENCES Personne(id) ON DELETE CASCADE
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE employe (
        id VARCHAR(4),
        DateEmb VARCHAR(40),
        Username VARCHAR(40),
        empPwd VARCHAR(40),
        acces INTEGER,
        FOREIGN KEY (id) REFERENCES Personne(id) ON DELETE CASCADE
    )
    """
)
createTableQuery.exec("""
    CREATE TABLE "Film" (
        idf INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        NomFilm VARCHAR(40),
        DureeFilm VARCHAR(40),
        DescFilm VARCHAR(255))
    """)

createTableQuery.exec("""
    CREATE TABLE "CatFilm" (
        idf INTEGER,
        Animation INTEGER,
        Comedie	INTEGER,
        Documentaire INTEGER,
        Drame INTEGER,
        Fantaisie INTEGER,
        Horreur INTEGER,
        ScienceFiction INTEGER,
        Thriller INTEGER,
        FOREIGN KEY (idf) REFERENCES Film(idf) ON DELETE CASCADE)
    """)

# Table contenant la liste des types de catégories de films
#createTableQuery.exec("""CREATE TABLE "Categories" ("categories" VARCHAR(60) UNIQUE)""")

# Table contenant la liste des types d'accès
createTableQuery.exec("""CREATE TABLE "CatAcces" ("list" VARCHAR(60) UNIQUE)""")

insquery = QSqlQuery()  # Insertion de la liste déroulante des accès par une table
insquery.prepare("""INSERT INTO CatAcces (list) 
                VALUES ('Consultant'), ('employé'), ('Direction'), ('Sécurité'), ('Admin')""")
insquery.exec()
# Insertion de la liste des catégorie dans la table CatFilm
#insquery.prepare("""INSERT INTO Categories (categories)
#                VALUES ('Animation'), ('Comedie'), ('Documentaire'),
#                 ('Drame'), ('Fantaisie'), ('Horreur'),
#                  ('ScienceFiction'), ('Thriller')""")
#insquery.exec()

print(con.tables())
