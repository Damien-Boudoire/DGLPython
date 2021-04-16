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

cursor.execute("SELECT unit.name "\
               "FROM student, unit "\
               "WHERE student.current_unit_fk = unit.id "\
               "AND student.id = {0};".format(student_id))

for row in cursor:
    print(row[0])

cursor.close()
connexion.close()