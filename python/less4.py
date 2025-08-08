# операторы присваивания

# a = 1

# a += 1 
# -=
# *=
# /=
# %=
# **=
# //=
# a = a + 1

# print (a)


# print('text' + 'text')
# text = 'text'
# # text = text + ' new'
# text += ' OLD'
# print(text)

# print('~' * 20)

# symbol = '-'
# symbol *= 20
# print(symbol)


##########################################

# операторы принадлежности
# in    not in
# есть ли что-то в чемто

# text = 'I love Python!'
# print ('love' in text)
# print ('Love' in text)


##########################################

# оператор индентичности
# is    is not
# сравнение

# a = 'text'
# b = 'text'
# c = 10
# print(a is b)
# print(id(b))
# print(id(a))
# print(c is not b)


##########################################

# Способы ввода данных
# Клавиатура, чтение из файла, БД, API

# user_name = input('What is uour name?')
# print('Hello', user_name, '!')


# в режиме input результат всегда будет строка
# user_input = input('Enter numbre:')
# print(type(user_input))
# print(user_input + 2)  #будет ошибка


# Преобразование типов данных

# a = '1'
# print(type(a))
# a = int(a)
# print(type(a))
# a = str(a)
# print(type(a))

# b = 'True'
# print(type(b))
# b = bool(b)
# print(type(b))

# c = 1
# c = float(c)
# print(type(c))
# print(c)

# user_input = input('Enter numbre:')
# user_number = int(user_input)
# print(type(user_number))
# print(user_number + 2)  
# # при приобразование в int нужно быть уверенным что приобразуемое может приобразоваться



#########################################

# типа данных в Puthon

# number - число
# string - строка
# boolean - логическое
# float - число с плавающей точкой
# list - список, массив
# dictionary - словарь
# tuple - кортеж
# set - множество


# Список - List
# структура данных для хранения последовательностей. Массив

# my_list = [1, 2, 3, None, 'Text', False, 2.34, True]
# print(my_list)
# print(my_list[4])
# print(my_list[0])
# print(my_list[-1])

# my_list[4] = 42
# print(my_list)
# print(my_list[4])

# my_list_2 = []
# my_list_3 = list()

# my_list_3.append('Test1') # добавление в конец
# my_list_3.append(13)
# print(my_list_3)

# print(len(my_list_3)) # считает кол-во элементов
# print(len(my_list_2))

# print(my_list.index(42)) # найти индекс элемента

# poped = my_list.pop(4) #удаляет элемент по индексу и помешает в переменную
# print(my_list)
# print(poped)

# print('Test1' in my_list_3)


# Кортеж - Tuple
# хранят данные типов
# Неизменяемы
# занимают меньший размер

# my_tuple = ('1', 2, 3, None, 'Text', False, 2.34, True)
# print(my_tuple)
# print(my_tuple[1])
# print(my_tuple[-1])

# # my_tuple[4] = 42 #ошибка. кортеж неизменяем


# my_tuple2 = ()
# my_tuple3 = tuple()
# my_tuple2 = (1,2,3,1,2,5,1) # не изменение. Перезаписывает
# print(my_tuple2)
# print(my_tuple2.count(1)) # считает сколько раз элемент встречается в кортеже
# print(my_tuple2.index(2)) # какой индекс у элемента


# llist = [56]
# print(llist)
# ttuple = (56,) # если в кортеже 1 значение и без запятой, то кортеж не присваивется
# print(ttuple)



##################################

# Множество - set
# содержит в себе только неповторяюшиеся элементы
# не гарантирует порядок элементов

# print('          ')
# my_set = {'1', 1, 2, 2, 3, None, 'Text', False, 2.34, True}
# # print(my_set[2]) #ошибка
# my_set.add(4) #добавление элемента
# print(my_set) # положение элементов изменено


# list1 = [1,2,3,5,6,1,5,2,2]
# list1 = set(list1) # оставит только уникальные значения
# print(list1)
# list1 = list(list1)
# print(list1)

# list2 = list(set([1,2,3,5,6,1,5,2,2])) # оставит только уникальные значения
# print(list2)

# my_set_empty = set() #только так создается пустой set



# словари - Dictionary
# коллекция объектов с доступом к ним по ключу. Ассоциативный массив. Хещ таблица

# my_dict = {'one': 'value', 'two': 'value2', 2: 3}
# print(my_dict)
# print(my_dict[2])
# print(my_dict['one'])

# print(len(my_dict))

# my_dict['two'] = 'TEST'
# my_dict['three'] = True
# my_dict['four'] = [1,2,3]
# my_dict['five'] = {1,4,5}
# my_dict[3] = False
# my_dict[False] = 'False'
# my_dict[3.31] = True
# my_dict[(1,3)] = 'Abra'
# my_dict[5] = {1: 2}
# print(my_dict)

# print(my_dict.keys()) # ключи словаря
# print(my_dict.values()) #значения словаря
# print(my_dict.items()) #пары ключ и значения