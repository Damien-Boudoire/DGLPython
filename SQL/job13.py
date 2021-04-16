import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

job_id = int(input("Entrez un identifiant de job :"))

cursor.execute("SELECT job.name, skill.name "\
               "FROM job, job_skill, skill "\
               "WHERE job.id = job_skill.job_fk "\
               "AND skill.id = job_skill.skill_fk "\
               "AND job.id = {0};".format(job_id))

for row in cursor:
    print(row[0], row[1])

cursor.close()
connexion.close()