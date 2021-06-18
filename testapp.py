import datetime
import time

import main as m
import unittest

from PyQt5.QtSql import QSqlQuery # Besoin de QSqlQuery
import re # Utilisation de regex pour le test de courriel
import freezegun # Utilisation de freezegun pour les tests de date et heure
import datetime as dt

class TestProgramme(unittest.TestCase):
    query = QSqlQuery
    p = query("SELECT * FROM Personne")
    u = query("SELECT * FROM employe")


    def testlogin(self): #test de login
        print ("test de la fenêtre de login")
        self.u.exec()
        lu = 'consultant'
        lp = 'Nouveau123'
        message = 'Cela ne correspond pas'
        while self.u.nextResult():
            self.assertEqual(self.u.value('Username'), lu, message)
            self.assertEqual(self.u.value('empPwd'), lp, message)
        print ("test de login complété")

    def testP(self): # test de la classe Personne
        lp = [] # liste des prénom
        ln = [] # liste des nom
        ls = [] # liste des sexe
        print("Debut du test de la classe Personne")
        self.p.exec()
        while self.p.next(): # Ajoute aux listes les informations recueillie dans SQLite et les print
            lp.append(self.p.value('Prenom'))
            ln.append(self.p.value('Nom'))
            ls.append(self.p.value('Sexe'))
            m.Personne.sexe = self.p.value('Sexe')
            m.Personne.prenom = self.p.value('Prenom')
            m.Personne.nom = self.p.value('Nom')
        print(lp)
        print(ln)
        print(ls)
        if m.Personne.sexe == -4: # Ne met pas les autres options car seul cette option est présente par défaut dans SQL
            vs = "Préfère ne pas répondre"
        else :
            vs = 0 # Si la fonction Personne.sexe n'est pas bonne, cela va retourner un message d'erreur
        svalidation = "Préfère ne pas répondre"
        consultant = "consultant"
        message = 'Cela ne correspond pas'
        self.assertEqual(vs, svalidation, message) # validation de la fonction sexe
        self.assertEqual(m.Personne.prenom, consultant, message) # Validation de la fonction prenom
        self.assertEqual(m.Personne.nom, consultant, message) # Validation de la fonction nom
        print("Fin des tests de la classe Personne")

    def testC(self): # test de la classe Client (La classe employé est semblable)
        print('Test de la classe Client')
        # test du mot de passe client
        m.client.clientPwd = '12345678'
        pwd = '1234567'
        message = 'Le mot de passe doit avoir au moins 8 caractères'
        self.assertGreater(m.client.clientPwd, pwd, message) # validation si le mot de passe inscrit est d'au moins 8 caractères
        # test du courriel
        m.client.courriel = 'bob@bobby.com'
        regexmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' #validation du regexmail sur le courriel
        if re.search(regexmail, m.client.courriel):
            print("Le courriel est valide")
        else :
            print("le courriel n'est pas valide")
        # test de la date d'inscription
        print("test de la date")
        m.client.dateInsc = dt.date.today()
        assert m.client.dateInsc == dt.date.today() # Validation que la date inscrite est la même
        print(m.client.dateInsc)
        print("fin des tests de la classe client")

    def testF(self): # test de la classe film
        print("Debut des tests de la class Film")
        m.Film.dureeFilm = datetime.datetime.now()
        assert m.Film.dureeFilm == datetime.datetime.now() #Valide que l'heure inscrit est la même
        print (m.Film.dureeFilm)

        print("Fin des tests des films")




if __name__ == "__main__":
    unittest.main()