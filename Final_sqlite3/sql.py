import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("data.db")
print("Database created")

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
    """)
createTableQuery.exec(
    """
    CREATE TABLE CartedeCredits (
        NumeroCC int NOT NULL,
        DateCC int NOT NULL,
        CodeCC int NOT NULL,
        id INTEGER,
        PRIMARY KEY (NumeroCC),
        CONSTRAINT FK_PersonOrder FOREIGN KEY (id)
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
        CONSTRAINT FK_PersonOrder FOREIGN KEY (id)
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
        CONSTRAINT FK_PersonOrder FOREIGN KEY (id)
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
        DateFin acces(40) NOT NULL,
        id INTEGER,
        PRIMARY KEY (Username),
        CONSTRAINT FK_PersonOrder FOREIGN KEY (id)
        REFERENCES Personne(id)
    )
    """
)
createTableQuery.exec(
    """
    CREATE TABLE Film (
        NomFilm VARCHAR(40) NOT NULL,
        DureeFilm VARCHAR(40) NOT NULL,
        DescFilm VARCHAR(40) NOT NULL,
        CatFilm acces(40) NOT NULL,
        id INTEGER,
        PRIMARY KEY (Username),
        CONSTRAINT FK_PersonOrder FOREIGN KEY (id)
        REFERENCES Personne(id)
    )
    """
)
print(con.tables())
