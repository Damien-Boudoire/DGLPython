import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

job_name = input("Entrez un nom de job : ")

cursor.execute("SELECT job.name, unit.name "\
               "FROM unit, job "\
               "WHERE unit.id = job.unit_fk "\
               "AND job.name = '%s';"%job_name)
for row in cursor:
    print(row[0], row[1])

cursor.close()
connexion.close()