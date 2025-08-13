# summer = True
# if summer is True:
#     print ('The weather is fine')
# else:
#     print('The weather is not fine')


# summer = True
# if summer:  #такое условие равно if True (или False если присвоить)
#     print ('The weather is fine')
# else:
#     print('The weather is not fine')

# a = 'Stroka'
# if a: #а воспринимается как True. Если переменная пустая или 0 то false
#     print('...')



########################################################

# Встроенные функции

# numb = [1, 22, 432, 12, 221, 2, 3]
# print(max(numb)) # показывает максимальное число 
# print(min(numb)) # минимальное число
# print(sum(numb)) # сумма

# a = 1 / 3
# print(round(a, 3)) #округлить до 3 символов после запятой

# print(abs(1)) #модуль от числа (отклонение)

# print(sorted(numb)) #сортировка по порядку (возростанию)
# print(sorted(numb, reverse=True)) #обратная сортировка

# print(numb)
# numb = sorted(numb)     # перезапись как отсортированая
# print(numb)
# numb.sort()             # перезапись как отсортированая
# print(numb)
# numb.sort(reverse=True) # перезапись как отсортированая
# print(numb)



########################################################


# Map

# Применение операции к каждому элементу
# аналог цикла for


# my_list =[1, 2, 3, 4]

# new_list = []
# for x in my_list:
#     new_list.append(x * 2)
# print(new_list)


# def mult_by_2(x):
#     return x * 2
# new_list2 = map(mult_by_2, my_list) # для каждого элемента массива отраб функция
# print(list(new_list2))


# new_list_3 = map(lambda x: x * 2, my_list) 
# #lambda говорит что будет короткая функция которую проше не обьявлять
# print(list(new_list_3))

# print(list(map(lambda x: x * 2, my_list)))


# new_list_4 = map(lambda x: x * 5 if x > 10 else x * 2, my_list)
# # тернарный оператор
# print(list(new_list_4))


# b = 1 if len(my_list) > 4 else 5
# print(b)



########################################################

# filter


# my_list = [1, 2, 3, 4, 5, 6, 7, 8]


# new_list = []
# for x in my_list:
#     if x % 2 == 0:
#         new_list.append(x)
# print(new_list) #Взяты только четные числа

# #

# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else: 
#         return False
    
# new_list_2 = filter(is_even, my_list) 
# # для каждого элемента применяется фильтр. 
# # Если получет True то попадает в новый список
# print(list(new_list_2))

# #

# def is_even(x):
#     if x % 2 == 0:
#         return True
#     return False #условие упрошено убрав else

# new_list_3 = filter(is_even, my_list) 
# print(list(new_list_3))

# #

# def is_even(x):
#     return x % 2 == 0
# #ещё большее упрошение за счет дальнейшего исп True и False 

# #

# new_list_4 = filter(lambda x: x % 2 == 0, my_list) 
# print(list(new_list_4))



########################################################


# Datetime

# import datetime

# time_now = datetime.datetime.now()
# print(time_now)
# print(time_now.hour)
# print(time_now.year)
# print(time_now.isoweekday())
# print(time_now.timestamp())

# easy_date = datetime.datetime(1960, 1, 15)
# print(easy_date)


# my_time = '2023/06/02 12 hours, 30 minutes, 12 sec'
# python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M minutes, %S sec')
# print(python_date)
# print(python_date.month)

# human_date = python_date.strftime('Year: %y, month: %B, day: %d')
# print(human_date)