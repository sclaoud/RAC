import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# Crée la connection
try:
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("data.db")
    print("Connection à la BD")
    pq = QSqlQuery()
    pq.exec("PRAGMA foreign_keys")
    if pq.value('foreign_keys') == 1:
        print('Foreign_key actifs')
    if pq.value('foreign_keys') == 0:
        print('Foreign_key désactivé')
    pq.exec("PRAGMA foreign_keys = ON")
    con.open()
    print(con.lastError().text())
#    print(pq.lastError().text())

finally:
    # Si cela ne fonctionne pas, retourne une erreur
    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

# Validation des tables déjà créer et skip au besoin
lt = con.tables()
if not 'Personne' in lt:
    # Création des tables si celle-ci n'existe pas dans la BD
    createTableQuery = QSqlQuery()
      # Crée la table Personne, table principale
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
if not 'CartedeCredits' in lt:
      # Crée la table CartedeCredits, enfant de Personne
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
if not 'Client' in lt:
      # Crée la table client, enfant de Personne
    createTableQuery.exec(
        """
        CREATE TABLE Client (
        "id" VARCHAR(4),
        "DateInsc" VARCHAR(40),
        "Courriel" VARCHAR(255) UNIQUE,
        "ClientPwd" VARCHAR(40),
        FOREIGN KEY("id") REFERENCES "Personne"("id") ON DELETE CASCADE
        )
        """
    )
if not 'Acteurs' in lt:
      # Crée la table acteurs, enfant de Personne
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
if not 'employe' in lt:
      # Crée la table des employé, enfant de Personne
    createTableQuery.exec(
        """
        CREATE TABLE employe (
            id VARCHAR(4),
            DateEmb VARCHAR(40),
            Username VARCHAR(40),
            empPwd VARCHAR(40),
            Acces VARCHAR(60),
            FOREIGN KEY (id) REFERENCES Personne(id) ON DELETE CASCADE
            FOREIGN KEY("Acces") REFERENCES CatAcces(list)
        )
        """
    )
    # Insert les users test dans les tables créer
    insquery = QSqlQuery()
    insquery.prepare("""INSERT INTO Personne (Prenom, Nom, Sexe, cbc, cba, cbe)
                      VALUES ('admin', 'admin', '-4', '0', '0', '2'),
                      ('consultant', 'consultant', '-4', '0', '0', '2')""")
    insquery.exec()
    insquery.prepare("""INSERT INTO employe (id, Username, empPwd, Acces)
                      VALUES ('1' ,'admin', 'Bonjour123', 'Lecture/Ecriture'),
                      ('2', 'consultant', 'Nouveau123', 'Lecture')""")
    insquery.exec()

if not 'Film' in lt:
      # Crée la table des informations des films
    createTableQuery.exec("""
        CREATE TABLE "Film" (
            idf INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            NomFilm VARCHAR(40),
            DureeFilm VARCHAR(40),
            DescFilm VARCHAR(255))
        """)
if not 'CatFilm' in lt:
      # Crée la table des catégorie de films
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
if not 'CatAcces' in lt:
    # Table contenant la liste des types d'accès
    createTableQuery.exec("""CREATE TABLE "CatAcces" ("list" VARCHAR(60) UNIQUE)""")

    insquery = QSqlQuery()  # Insertion de la liste déroulante des accès par une table
    insquery.prepare("""INSERT INTO CatAcces (list) 
                    VALUES ('Lecture/Ecriture'), ('Lecture')""")
    insquery.exec()

