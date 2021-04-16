import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

skill_id = int(input("Entrez un identifiant de compétence :"))

cursor.execute( "SELECT student_id, points "\
                "FROM (SELECT student.id AS student_id, SUM(earned) AS points "\
                    "FROM student, unit, job, job_skill "\
                    "WHERE student.current_unit_fk = unit.id "\
                    "AND job.unit_fk = unit.id "\
                    "AND job_skill.job_fk = job.id "\
                    "AND job_skill.skill_fk = {0} "\
                    "GROUP BY student.id "\
                    ") AS student_skill_points "\
                "WHERE points >= all ((SELECT SUM(earned) AS points "\
                                    "FROM student, unit, job, job_skill "\
                                    "WHERE student.current_unit_fk = unit.id "\
                                    "AND job.unit_fk = unit.id "\
                                    "AND job_skill.job_fk = job.id "\
                                    "AND job_skill.skill_fk = {0} "\
                                    "GROUP BY student.id "\
                                    "));".format(skill_id))

for row in cursor:
    print(row[0], row[1])

cursor.close()
connexion.close()