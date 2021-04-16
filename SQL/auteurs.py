import mysql.connector

init_connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234"#,
#    auth_plugin='mysql_native_password'
)

init_curseur = init_connexion.cursor()
init_curseur.execute("CREATE DATABASE IF NOT EXISTS Runtrack1;")
init_curseur.close()
init_connexion.commit()
init_connexion.close()


connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="Runtrack1"
#    auth_plugin='mysql_native_password'
)
curseur = connexion.cursor()

request_drop_tables="DROP TABLE IF EXISTS Livre; DROP TABLE IF EXISTS Auteur;"
curseur.execute(request_drop_tables)
curseur.close()
connexion.close()


connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="Runtrack1"
#    auth_plugin='mysql_native_password'
)
curseur = connexion.cursor()

creation_auteurs_request = "CREATE TABLE IF NOT EXISTS Auteur("\
                                "id INT NOT NULL AUTO_INCREMENT ,"\
                                " nom VARCHAR(64),"\
                                " prenom VARCHAR(64),"\
                                " PRIMARY KEY(id));"

creation_livres_request = "CREATE TABLE IF NOT EXISTS Livre ("\
                                "id INT NOT NULL AUTO_INCREMENT,"\
                                " titre VARCHAr(128),"\
                                " auteur_id INT,"\
                                "PRIMARY KEY(id),"\
                                " FOREIGN KEY (auteur_id) REFERENCES Auteur(id));"

curseur.execute(creation_auteurs_request)
curseur.execute(creation_livres_request)

auteurs=[{"prenom" : "Philip K.",   "nom" : "Dick", "livres": ["Le maitre du haut château", "Ubik", "Blade Runner"]},
         {"prenom" : "Isaac",       "nom" : "Asimov", "livres": ["Fondation", "Le cycle des robots"]},
         {"prenom" : "Ray",         "nom" : "Bradbury", "livres": ["Chroniques martiennes", "Fahrenheit 451"]},
         {"prenom" : "Kim Stanley", "nom" : "Robinson", "livres": ["Mars la Rouge", "Mars la verte", "Mars la bleu", "Chroniques des années noires"]},
         {"prenom" : "Hal",         "nom" : "Duncan", "livres": ["Velum", "Encre"]}]



insert_auteurs_request = "INSERT INTO Auteur (nom, prenom) VALUES"
insert_livres_request = "INSERT INTO Livre (titre, auteur_id) VALUES"
auteur_id = 1
for auteur in auteurs[:-1]:
    insert_auteurs_request += "('%s', '%s'), "%(auteur["nom"], auteur["prenom"])
    for titre in auteur["livres"]:
        insert_livres_request +="('%s', '%s'),"%(titre, auteur_id)
    auteur_id += 1
insert_auteurs_request += "('%s', '%s');"%(auteurs[-1]["nom"], auteurs[-1]["prenom"])
for titre in auteurs[-1]["livres"][:-1]:
    insert_livres_request +="('%s', '%s'),"%(titre, auteur_id)
insert_livres_request += "('%s', '%s');"%(auteurs[-1]["livres"][-1], auteur_id)

#print(insert_livres_request)

curseur.execute(insert_auteurs_request)
curseur.execute(insert_livres_request)

curseur.execute("SELECT * FROM Auteur")
for row in curseur:
    #print(row)
    continue

curseur.execute("SELECT * FROM Livre")
for row in curseur:
    #print(row)
    continue

connexion.commit()


auteur_nom = input("De quel auteur voulez-vous voir la bibliographie ? ")

select_auteur_livres = "SELECT Livre.titre "\
                        "FROM Livre, Auteur "\
                        "WHERE Livre.auteur_id = Auteur.id "\
                        "AND Auteur.nom ='%s';"%auteur_nom
curseur.execute(select_auteur_livres)
for titres in curseur:
    for e in titres:
        print(e)

curseur.close()
connexion.close()
