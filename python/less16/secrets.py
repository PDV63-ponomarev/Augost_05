# import mysql.connector as mysql
# import creds

# db = mysql.connect(
#     user=creds.user,
#     passwd=creds.passwd,
#     host=creds.host,
#     port=creds.port,
#     database=creds.database
# )

# cursor = db.cursor(dictionary=True)
# cursor.execute('SELECT * FROM students WHERE name = "Billy"')
# data = cursor.fetchall()
# print(data)


import mysql.connector
from mysql.connector import Error

print("Тест подключения начат")

try:
    # Попробуйте подключиться без базы данных сначала
    connection = mysql.connector.connect(
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',  # или ваш хост
        user='st-onl',
        password='AVNS_tegPDkI5BlB2lW5eASC',
        connection_timeout=5
    )
    
    if connection.is_connected():
        print("Базовое подключение работает!")
        connection.close()
        
except Error as e:
    print(f"Ошибка: {e}")

print("Тест завершен")