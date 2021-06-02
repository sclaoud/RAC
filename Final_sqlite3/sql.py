import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel

# Query pour les demandes ID universel

# Create the connection
try:
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("data.db")
    print("Database created")
    con.open()

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
        Prenom VARCHAR(40) NOT NULL,
        Nom VARCHAR(40) NOT NULL,
        Sexe int NOT NULL
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE CartedeCredits (
        id INTEGER,
        NumeroCC int NOT NULL,
        DateCC int NOT NULL,
        CodeCC int NOT NULL,
        PRIMARY KEY (NumeroCC),
        FOREIGN KEY (id) REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Client (
        id INTEGER,
        DateInsc int NOT NULL,
        Courriel VARCHAR(255) NOT NULL,
        ClientPwd VARCHAR(40) NOT NULL,
        PRIMARY KEY (courriel),
        FOREIGN KEY (id) REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Acteurs (
        id INTEGER,
        TitreFilm VARCHAR(40) NOT NULL,
        Personnage VARCHAR(40) NOT NULL,
        DateDebut VARCHAR(40) NOT NULL,
        DateFin VARCHAR(40) NOT NULL,
        Cachet VARCHAR(40) NOT NULL,
        PRIMARY KEY (Personnage),
        FOREIGN KEY (id) REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE employe (
        id INTEGER,
        DateEmb VARCHAR(40) NOT NULL,
        Username VARCHAR(40) NOT NULL,
        empPwd VARCHAR(40) NOT NULL,
        DateFin VARCHAR(40) NOT NULL,
        acces VARCHAR(40) NOT NULL,
        PRIMARY KEY (Username),
        FOREIGN KEY (id) REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE "Film" (
    	"idf"	INTEGER NOT NULL UNIQUE,
        "NomFilm"	VARCHAR(40) NOT NULL,
        "DureeFilm"	VARCHAR(40) NOT NULL,
        "DescFilm"	VARCHAR(255) NOT NULL,
        "CatFilm"	VARCHAR(40) NOT NULL,
        PRIMARY KEY("idf" AUTOINCREMENT)
	)
    """
)
createTableQuery.exec(
    """
    CREATE TABLE "CatFilm" (
        "idf"	INTEGER NOT NULL,
        "Animation"	INTEGER NOT NULL,
        "Fantaisie"	INTEGER NOT NULL,
        "Science-Fiction"	INTEGER NOT NULL,
        "Horreur"	INTEGER NOT NULL,
        "Drame"	INTEGER NOT NULL,
        "Thriller"	INTEGER NOT NULL,
        "Documentaire"	INTEGER NOT NULL,
        "Comédie"	INTEGER NOT NULL,
        FOREIGN KEY(idf) REFERENCES Film (idf)
    )
    """
)

print(con.tables())
