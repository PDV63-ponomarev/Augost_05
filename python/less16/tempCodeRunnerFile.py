import mysql.connector as mysql
import creds


db = mysql.connect(
    user = creds.user,
    passwd = creds.passwd,
    host = creds.host,
    port = creds.port,
    database = creds.database
)

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM students WHERE name = "Billy"')
data = cursor.fetchall()
print(data)
