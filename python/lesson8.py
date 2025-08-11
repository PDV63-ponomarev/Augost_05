# Generator fuction


# Generator function

# def generator_text(text1, text2):
#     return f'Text consists on the wrods:{text1} and {text2}'

# print(generator_text('Ivan', 'Ivanov'))


# n = 2
# progression = []
# num = 1
# while num < 200:
#     progression.append(num)
#     num += n
    # print(progression)


# def progr(limit=100):
#     n = 2
#     num = 1
#     count = 1
#     while count < limit:
#         yield num # команда генератора, возврашает значен переменной и продолж
#         num += n
#         count += 1

# count = 1
# for number in progr(100000100): #нереально большой поток данных (бесконечных)
#     if count == 1000000: # на миллионном числе остановится и покажет его
#         print(number)
#         break
#     count += 1


# print(type(progr(10))) #имеет класс генератор
# print(list(progr(10))) #преобр значение генератора в список и показывает

# for number in progr(10):
#     print(number)
# print(list(progr(10)))



##########################################################


# Modules

# не все функции предустановлены. Для некоторых функций нужен импорт нужного модуля
# модули - библиотека


# import random     # моудль рандомов
# import os       # модуль взаимодействия с ОС
# import sys      # модуль системы
# import selenium # если модуль не предустоновленный надо его установит

###
# установка модуля из терминала: pip install selenium
# команда для установки можно найти на pypi.org
###


# random.random()  #в модуле рандом, функция рандом генер. ранд данные

# print(random.random()) #по умолч от 0 до 1
# print(int(random.random() * 100)) #целое число от 0 до 100

# print(random.randint(0, 5)) #рандом целого число от и до включительно
# print(random.randrange(0, 5)) #рандом целого число от и до не-включительно
# print(random.randrange(0, 11, 2)) 
# #рандом целого число от 0 и 11 до не-включительно c шагом каждый 2


# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# print(random.choice(users)) # выбор значения из списка
# print(users[random.randrange(0, len(users))]) # выбор значения из списка


###############

# import moduler.helper as helper   # модуль создан вручную. файл лежит тамже где и прогр
# через as можно переименовать модуль или функцию

# from moduler import helper        # модуль создан вручную. файл лежит тамже где и прогр

# helper.assist()
# print(helper.variable)



# from moduler.helper import assist  # импорт конкретной функции 

# assist()


