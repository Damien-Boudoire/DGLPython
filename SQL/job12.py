import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

student_id = int(input("Entrez un identifiant de groupe :"))

cursor.execute("SELECT job.name, unit.name "\
               "FROM registration AS rg, job, unit "\
               "WHERE rg.job_fk = job.id "\
               "AND job.unit_fk = unit.id "\
               "AND group_id = {0};".format(student_id))

for row in cursor:
    print(row[0], row[1])

cursor.close()
connexion.close()