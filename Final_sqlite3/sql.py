import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

#Racroucie a utiliser dans tout le code pour QsqlQuery
query = QSqlQuery()

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
        NumeroCC int NOT NULL,
        DateCC int NOT NULL,
        CodeCC int NOT NULL,
        id INTEGER,
        PRIMARY KEY (NumeroCC),
        CONSTRAINT Personne FOREIGN KEY (id)
        REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Client (
        DateInsc int NOT NULL,
        Courriel VARCHAR(255) NOT NULL,
        ClientPwd VARCHAR(40) NOT NULL,
        id INTEGER,
        PRIMARY KEY (courriel),
        CONSTRAINT Personne FOREIGN KEY (id)
        REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Acteurs (
        TitreFilm VARCHAR(40) NOT NULL,
        Personnage VARCHAR(40) NOT NULL,
        DateDebut VARCHAR(40) NOT NULL,
        DateFin VARCHAR(40) NOT NULL,
        Cachet VARCHAR(40) NOT NULL,
        id INTEGER,
        PRIMARY KEY (Personnage),
        CONSTRAINT Personne FOREIGN KEY (id)
        REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE employe (
        DateEmb VARCHAR(40) NOT NULL,
        Username VARCHAR(40) NOT NULL,
        empPwd VARCHAR(40) NOT NULL,
        DateFin VARCHAR(40) NOT NULL,
        acces VARCHAR(40) NOT NULL,
        id INTEGER,
        PRIMARY KEY (Username),
        CONSTRAINT Personne FOREIGN KEY (id)
        REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE "Film" (
        "NomFilm"	VARCHAR(40) NOT NULL,
        "DureeFilm"	VARCHAR(40) NOT NULL,
        "DescFilm"	VARCHAR(255) NOT NULL,
        "CatFilm"	NUMERIC NOT NULL,
        PRIMARY KEY("NomFilm")
	)
    """
)
print(con.tables())
