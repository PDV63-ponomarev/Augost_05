# Декораторы --- Decorators



# def calc():
#     print(1+1)

# calc()
# print(calc)
# new_calc = calc
# print(new_calc)
# new_calc() # функция равна функции calc 


##


# def greet():
    
#     def hello():
#         return 'Hello'
    
#     return hello() # возврашает результат подфункции

# print(greet())


##


# def outher():

#     def inner():
#         result = 2 + 5
#         return result
    
#     return inner #вовзараем переменную храняшую внутр функцию

# print(outher)     # внутри переменной хранится функция
# print(outher())   # результат работы функци другая функция 
# print(outher()()) # выполняется подфункция

# inner_funct = outher() # переменной присваивается результат работы функции (результат функция)
# print(inner_funct()) # Переменная выполняется как функция


##


# def func1(give_func):
#     print('before')
#     give_func()
#     print('after')

# def simple_1():
#     print('Simple1')

# def simple_2():
#     print('Simple2')

# simple_1()
# simple_2()

# func1(simple_2) #передача в функцию другой функции как параметр
# func1(simple_1)


# def simple_3():
#     print('I')
#     print('function')
#     print('number')
#     print('3')

# func1(simple_3)


##


# def add_text(func):
    
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper

# def simpl1():
#     print('ONE')

# simpl1()
# simpl1 = add_text(simpl1)
# simpl1()


# def simpl2():
#     print('TWO')

# simpl2()
# simpl2 = add_text(simpl2)
# simpl2()


##


# def add_text(func):
    
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper


# @add_text # декоратор. Присваивает функцию ниже как аргумент для заданной функции
# def simpl1():
#     print('ONE')

# @add_text # с помошью заданной функции обрабатывает функцию нижу
# def simpl2():
#     print('TWO')

# simpl1() # = add_text(simpl1)()
# simpl2()


##


# def add_logs(func):
    
#     def wrapper():
#         print(f'function {func.__name__} started') # достаем имя функции
#         result = func()
#         print(f'finiched {func.__name__}')
#         return result
#     return wrapper

# @add_logs
# def simpl1():
#     print('ONE')

# @add_logs
# def simpl2():
#     print('TWO')

# simpl1()
# simpl2()


##


# def add_logs(func):
    
#     def wrapper(*args):
#         print(f'function {func.__name__} started') # достаем имя функции
#         result = func(*args)
#         print(f'finiched {func.__name__}')
#         return result
#     return wrapper

# @add_logs
# def calc(x):
#     print(x * 2)

# @add_logs
# def calc2(x, y, z):
#     print(x * y - z)

# calc(3)
# calc2(3, 4, 3)



##########################################################


# list comprehension

# генератор списков
# составитель списков


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #1 умножечение через for. самый медленный
# new_list = []
# for x in my_list:
#     new_list.append(x * 2)
# print(new_list)

# #2 умножение через map. самый быстрый
# new_list = map(lambda x: x * 2, my_list)
# print(list(new_list))

# #3 умножение через list comprehension. средний по скорости
# new_list = [x * 2 for x in my_list]
# print(new_list)


##

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #1
# new_list = []
# for x in my_list:
#     if x % 2 == 0:
#         new_list.append(x)
# print(new_list)

# #2
# new_list = filter(lambda x: x % 2 == 0, my_list)
# print(list(new_list))

# #3
# new_list = [x for x in my_list if x % 2 == 0]
# print(new_list)


# new_generator = (x for x in my_list if x % 2 == 0)
# print(list(new_generator))


##########################################################

# Генерация словаря


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #1 
# new_dict = {}
# for x in my_list:
#     new_dict[x] = x * 3

# print(new_dict)


# #2
# new_dict = {x: x * 3 for x in my_list}

# print(new_dict)


#######


#1
# data = [('one', 'ONE'), ('two', 'TWO'), ('three', 'THREE')]

# new_dict = {}
# for key, value in data:
#     new_dict[key] = value

# print(new_dict)


#2
# data = [('one', 'ONE'), ('two', 'TWO'), ('three', 'THREE')]

# new_dict_2 = {key: value for key, value in data}

# print(new_dict_2)


#3
# data = [('one', 'ONE'), ('two', 'TWO'), ('three', 'THREE')]

# new_dict_3 = dict(data)

# print(new_dict_3)


#######


# country = ['USA', 'China', 'France']
# temps = [23, 33, 12]

# countr_dict = dict(zip(country, temps))
# print(countr_dict)

