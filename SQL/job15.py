import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

group_id = int(input("Entrez un identifiant de groupe :"))

cursor.execute("SELECT job.name "\
               "FROM registration AS rg, job "\
               "WHERE rg.job_fk = job.id "\
               "AND group_id = {0};".format(group_id))

for row in cursor:
    print(row[0])

cursor.close()
connexion.close()

cursor.close()
connexion.close()








