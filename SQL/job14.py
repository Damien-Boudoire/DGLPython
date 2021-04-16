import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

student_id = int(input("Entrez un identifiant d'étudiant :"))

cursor.execute("SELECT skill.name, SUM(earned) "\
                "FROM student, unit, job, job_skill, skill "\
                "WHERE student.current_unit_fk = unit.id "\
                "AND job.unit_fk = unit.id "\
                "AND job_skill.job_fk = job.id "\
                "AND job_skill.skill_fk = skill.id "\
                "AND student.id = {0} "\
                "GROUP BY skill.id;".format(student_id))

for row in cursor:
    print(row[0], row[1])

cursor.close()
connexion.close()








