import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="work",
    password="1234",
    database="laplateforme",
    auth_plugin='mysql_native_password'
)

cursor = connexion.cursor()

select_units="SELECT unit.name "\
            "FROM unit "\
            "WHERE unit.name LIKE '%Pool%';"

cursor.execute(select_units)
for unit in cursor:
    print(unit[0])

cursor.close()
connexion.close()