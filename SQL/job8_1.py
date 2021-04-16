import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

select_nb_students_by_promotion = "SELECT nb_students, promotion.name "\
                                  "FROM promotion, "\
                                    "(   SELECT COUNT(student.id) AS nb_students, promotion_fk "\
                                        "FROM student GROUP BY promotion_fk) AS studentsByPromotion "\
                                  "WHERE promotion.id = studentsByPromotion.promotion_fk;"

cursor.execute(select_nb_students_by_promotion)
for row in cursor:
    print(row[1], row[0])

cursor.close()
connexion.close()
