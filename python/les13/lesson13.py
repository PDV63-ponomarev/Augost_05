# открытие файла

# data_file = open('data.txt', 'r')
# data_file.read()
# print('123' + 123) # условная ошибка
# data_file.close() # при ошибке обработка кода остановится и файл не закроется


###################


# правильный способ открытия


## обрашение к файлу в директории где и файл.py
# import os
# script_dir = os.path.dirname(__file__)  # путь к файлу
# file_path = os.path.join(script_dir, "data.txt") # выставляет правильные / в пути к файлу
# new_file_path = os.path.join(script_dir, "data2.txt")
# ##


# def read_file():
#     # это гарантирует что файл будет закрыт из-за встроеного метода
#     with open(file_path, 'r') as data_file:
#         for line in data_file.readlines():
#             yield line

# for data_line in read_file():
#     with open(new_file_path, 'a') as new_file:
#         data_line = data_line.replace('.', '').replace(',', '') #удаляет . и ,
#         new_file.write(data_line)


#### файл в другой папке
# import os
# script_dir = os.path.dirname(__file__)
# homework_path = os.path.dirname(os.path.dirname(script_dir)) # поднимаемся до общей ветки
# data3_file_path = os.path.join(homework_path, 'homework\\learn_3', 'data3.txt')
# print(data3_file_path)

# with open(data3_file_path) as data3_file:
#     print(data3_file.read())



########################################



import datetime


now = datetime.datetime.now()
print(now)

today_mindnight = datetime.datetime.now().replace(hour=0, minute= 0, second=0, microsecond=0)
print(today_mindnight)

after = now - today_mindnight
print(after)
print(after.seconds)


print(now + datetime.timedelta(hours = 10)) #прибавить к дате 10 часов
print(now + datetime.timedelta(days = 20))