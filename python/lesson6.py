# условия и циклы

# Условия - Conditions
# if / elif / else


# user_inp = input('Your number: ')

# if user_inp.isnumeric():
#     user_inp = int(user_inp)
#     if user_inp == 1: 
#         print('Your number ONE')
#     elif user_inp == 2:
#         print('Your number TWO')
#     else: 
#         print('Your many')
# else:
#     print('This dont number')



################################################

# Циклы - loops
# for loop - цикл for


# names = ['Bob', 'Stive', 'John', 'Vi', 'Bill', 'Tom', 'James', 'Jimmi'] 

# for this_name in names: #для каждой Переменной в Массиве сделать:
#     print(this_name) # распечатать переменную


# for name in names:
#     name = name.replace('i', '*')
#     if name.startswith('J'):
#         print('Mr.', end=' ')
#     print(name)


################################################

# циклы со словарем

# pers = {'Bob': 111, 'Stive': 222, 'John': 333, 'Vi': 444, 
#         'Bill': 555, 'Tom': 666, 'James': 777, 'Jimmi': 888}

# for person in pers:
#     print(person) #печатает только ключи (имена)

# for person in pers.values():
#     print(person) #печатает только значения

# for person in pers:
#     print(f'{person} : {pers[person]}') #печать ключа и данных

# print(pers.items()) #печатает кортеж пар


# for person in pers.items(): #переводит словарь в кортеж из 2 элементов
#     name, height = person #присваивает переменным значениям кортежей
#     print(f'{name} : {height}')  

# for name, height in pers.items(): #упрошение пред кода
#         print(f'{name} : {height}')



# Распечатать все слова в которых есть буква о и выбросить из текста, 
# текст в конце распечатать

# text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris'

# words = text.split(' ')
# fin_words = []
# for word in words:
#     if 'o' in word:
#         print(word)
#     else:
#         fin_words.append(word)

# print(' '.join(fin_words))
