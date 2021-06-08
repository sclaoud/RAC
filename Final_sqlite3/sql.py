import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel, QSqlDriver, QSqlRecord, QSqlRelationalTableModel

# Query pour les demandes ID universel

# Create the connection
try:
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("data.db")
    print("Database created")
    con.open()
    con.exec("PRAGMA foreign_keys = ON")
    print(con.lastError().text())

finally:
    # Open the connection
    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

# Create a query and execute it right away using .exec()
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
	"id"	VARCHAR(4),
	"DateInsc"	VARCHAR(40),
	"Courriel"	VARCHAR(255),
	"ClientPwd"	VARCHAR(40),
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
createTableQuery.exec(
    """
    CREATE TABLE "Film" (
    	"idf"	INTEGER NOT NULL UNIQUE,
        "NomFilm"	VARCHAR(40),
        "DureeFilm"	VARCHAR(40),
        "DescFilm"	VARCHAR(255),
        "Animation"	INTEGER,
        "Fantaisie"	INTEGER,
        "Science-Fiction"	INTEGER,
        "Horreur"	INTEGER,
        "Drame"	INTEGER,
        "Thriller"	INTEGER,
        "Documentaire"	INTEGER,
        "Comedie"	INTEGER,
        PRIMARY KEY("idf" AUTOINCREMENT)
	)
    """
)
#Table contenant la liste des types d'accès
createTableQuery.exec(
    """
    CREATE TABLE "CatAcces" (
	"list"	VARCHAR(60) UNIQUE
    )
    """
)

insquery = QSqlQuery() # Insertion de la liste déroulante des accès par une table
insquery.prepare("INSERT INTO CatAcces (list) VALUES ('Consultant'), ('employé'), ('Direction'), ('Sécurité'), ('Admin')")
insquery.exec()

print(con.tables())
