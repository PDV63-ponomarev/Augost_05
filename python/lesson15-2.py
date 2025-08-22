import mysql.connector as mysql

db = mysql.connect(
    user = 'st-onl',
    passwd = 'AVNS_tegPDkI5BlB2lW5eASC',
    host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port = 25060,
    database = 'st-onl'
)

cursor = db.cursor(dictionary=True)

# cursor.execute('SELECT * FROM students')
# data = cursor.fetchall()
# for student in data:
#     print(student['name'])

cursor.execute('SELECT * FROM students WHERE id = 2')
data2 = cursor.fetchone()
cursor.execute('SELECT * FROM students WHERE id = 3')
data3 = cursor.fetchone()
print(data2, data3)


#уязвимый для взлома sql иньекцией
# query = f"SELECT * FROM users WHERE user = '{user}' and password = '{passw}'"
# cursor.execute(query.format(input('user'), input('password')))
# # user = Admin'; --  #Такая запись коментирует все что дальше имени
# # passw = False
# print(cursor.fetchall())


# Правильная запись
# query = f"SELECT * FROM users WHERE user = %s and password = %s"
# cursor.execute(query, (input('user'), input('password')))
# print(cursor.fetchall())


# cursor.execute("INSERT INTO students (namem, second_name, group_id) VALUES ('Ivan', 'Popov', 14)")
# cursor.execute("INSERT INTO students (namem, second_name, group_id) VALUES ('Ivan', 'Popov', 14)")
# cursor.execute("INSERT INTO students (namem, second_name, group_id) VALUES ('Ivan', 'Popov', 14)")
# db.commit()


# cursor.execute("INSERT INTO students (namem, second_name, group_id) VALUES ('Ivan', 'Popov', 14)")
# student_id = cursor.lastrowid #Запишет ид созданого 
# cursor.execute(f"SELECT * FROM students WHERE id = {student_id}")
# print(cursor.fetchone()) #покажет созданого


# insert_query = "INSERT INTO wtudents (name, second_name, group_id) VALUES (%s, %s, %s)"
# cursor.executemany(
#     insert_query, [
#         ('Ivan', 'Ivanow', 1),
#         ('Ivan', 'Popov', 2),
#         ('Vasya', 'Sidorov', 3),
#         ])


# select_query = '''
# SELECT *
# FROM students
# WHERE name = 'Ivan'
# AND first_name = 'Ivanov'
# OR first_name = 'Popov'
# '''


db.close()
