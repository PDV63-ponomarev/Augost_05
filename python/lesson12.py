# classes

# OOP - обьектно ориентированное программирование
# принципы ООП:
# Инкапсуляция (encapsulation)
# Наследование (inheritance)
# Полиморфизм (Polymorfism)


# 1
# Инкапсуляция
# Все данные объекта должны хранится в объекте. 
# Никто не может изменить данные объекта без его ведома.


# 2
# Наследование
# Объекты и их типы организуют иерархию типов. Дочерние типы наследют
# свою функциональность от родительского класса, расширяя и дополняя её


# 3
# Полиморфизм
# Способность классов менять своё поведение в зависимости от типов
# операции и операндов. Полиморфизм в программировании реализуется через 
# перегрузку метода, либо через его переопределение



# from abc import abstractmethod

# class Group:
   
#     pupils = True
#     school_name = 42
#     director = 'Marivanna'

#     def __init__(self, title, pupils_count, group_leader): 
#         self.title = title
#         self.pupils_count = pupils_count
#         self.group_leader = group_leader

#     def study(self):  
#         print('sit down and read')

#     @abstractmethod
#     def move(self):
#         pass 
  

# class PrimaryGroup(Group):
#     max_age = 11
#     min_age = 6
#     building_section = 'left'

#     def __init__(self, title, pupils_count, group_leader, class_room):
#         super().__init__(title, pupils_count, group_leader) 
#         self.class_room = class_room #наследование. Добавление к методу

#     def move(self): # полиформизм. Переопределение метода
#         print('Run fast')


# class HighGroup (Group):
#     max_age = 18
#     min_age = 14
 
#     def move(self): # полиформизм. Переопределение метода
#         print('Go slowly')


# first_a = PrimaryGroup('1 A', 15, 'DV', 112)
# # обьект представитель класса

# first_a.class_room = 1000
# print(first_a.class_room)
# # данные заменились. это не правильно, нужна защита



##################################



#данный способ чтения файла плохой, поскольку можно забыть закрыть файл
import json

# json.load() # преобразовывает содержимое в словарь
# json.loads() # преобразовывает содержимое строки в словарь

# def read_file(filename):
#     file_data = open(filename, 'r')
#     # data = file_data.read()
#     data = json.load(file_data) #преобразование строки из файла в словарь
#     file_data.close() # закрытие открытого файла
#     return data

# data1 = read_file('/project/Augost_05/python/les 12/data1.txt')
# data2 = read_file('/project/Augost_05/python/les 12/data2.txt')

# print(data1['Country'])
# print(data1['avg_temp'])
# print(data2['Country'])
# print(data2['avg_temp'])


######
# __ показывает что свойство приватным. его нельзя вызвать
# _ показывает что свойство защищено

class CountryData: 

    def __init__(self, filename):
        self.filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self.comfort = self.__is_comfort() 
    
  
    def __read_file(self):
        file_data = open(self.filename, 'r')
        data = json.load(file_data) 
        file_data.close() 
        return data
    
    def __is_comfort(self):
        return self.__avg_temp > 25
    

    @property #позволяет обращаться к защищеным аргументам (модулям)
    def data(self):
        return self.__data
    
    @property
    def country(self):
        return self.__country
    
    @property
    def avg_temp(self):
        return self.__avg_temp
    
    @property
    def comfort(self):
        return self._comfort

    @comfort.setter #функция изменения защищенного параметра
    def comfort(self, value):
        self._comfort = value


    def __str__(self): # метод 1 преобразования в строку обьекта
        return f'STR File {self.filename} with data {self.__data}'  

    def __repr__(self): # метод 2 преобразования в строку обьекта
        return f'REPR File {self.filename} with data {self.__data}'  
    
    def __lt__(self, obj): #метод сравнения меньше
        return self.avg_temp < obj.avg_temp
    
    def __le__(self, obj): #метод сравнения меньше или равно
        return self.avg_temp <= obj.avg_temp
    
    def __add__(self, obj): # метод сложения 
        return [self, obj]


class CountryDataWithMinTemp(CountryData):
    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']



data1 = CountryData('/project/Augost_05/python/les 12/data1.txt')
# print(data1.data)
# print(data1.country)
# print(data1.avg_temp)
# data1.comfort = False
# print(data1.comfort)

data2 = CountryData('/project/Augost_05/python/les 12/data2.txt')
# print(data2.data)
# print(data2.country)
# print(data2.avg_temp)
# print(data2.comfort)

data3 = CountryDataWithMinTemp('/project/Augost_05/python/les 12/data3.txt')
# print(data3.data)
# print(data3.avg_temp)
# print(data3.min_temp)
# print(data3.country)


# print(data1)

# print(data1 <= data2) #обращение к методу __le__
# print(data1 < data2) #обращение к методу __lt__

# #объявленные методы работ на меньше или равно, но отрабатывает и наоборот 
# print(data1 >= data2) #обращение к методу __le__
# print(data1 > data2) #обращение к методу __lt__

print (data1 + data2) #отрабатывает метод __repr__ и __add__
