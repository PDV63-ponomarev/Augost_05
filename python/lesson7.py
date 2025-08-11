# while and function


# while - цикл пока что-то не сделается

# i = 0

# while i < 5: #пока переменная меньше 5 будет выполн цикл
#     print('Num:' + f'{i}')
#     i += 1
# print('End')



# while True:
#     user_inp = input('Enter something: ')
#     if user_inp == 'exit':
#         break # принудительная остановка цикла
#     elif user_inp == 'scip':
#         continue # пропускает конкретно эту часть цикла
#     elif len(user_inp) > 10:
#         print('You ok')
#     else:
#         print('Input long')
# print('Good bye')



# text = 'Sed vitae justo malesuada, commodo end libero  eu, bibendum mauris'

# words = text.split(' ')
# fin_words = []
# for word in words:
#     if word == 'end':
#         break #при слове end заканчивает обработку
#     elif 'o' in word:
#         print(word)
#         continue    
#     fin_words.append(word)

# print(' '.join(fin_words))



###############################################

# Function (def)


# DRY - don't repeat yourself
# не повторяйся


# a = 1
# b = 4
# c = 6
# d = 2
# e = 0

# main_number = 47

# def calc(numb):
#     if e == 0:
#         print(numb)
#     else:
#         print(numb + main_number)

# calc(a)
# calc(b)
# calc(c)
# calc(d)


# def calc(numb):   #numb - параметры, то что присваивается при вызове - аргументы
#     if e == 0:
#         return numb
#     else:
#         return numb + main_number

# print(calc(a)) # а - аргумент
 
# result_b = calc(b) # b - аргумент
# print(result_b)


###########


# def print_words(first, second, third, fourth, fifth):
#     print(f'The first word is {first}, next word is {second}, {third}, {fourth} and {fifth}')
# print_words('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE')
# print_words(fifth='FIVE', first='ONE', fourth='FOUR', third='THREE', second='TWO')


############


# def power(number, degree=2):
#     return number ** degree

# print(power(2))
# print(power(2, 3))


############


# def example(e, f, g, ff = 'ONE', gg = 1):
#     print(e, f, g, ff, gg)

# example(2, 3, 4, gg = 100)
# example(20, f = 30, g = 40) 
#после введения наименового аргумента, остальные тоже должны быть наименованными


############


# def sum_all(*args): #принимает любое кол-во аргументов и суммирует их
#     print(args)
#     result = 0
#     for x in args:
#         result += x
#     print(result)

#     print(sum(args)) #эта функция выполн туже задачу. Суммирует содержимое

# sum_all(1, 2, 3, 4)


############


# def price_list(title, price):
#     print(f'Product {title} price is {price}')

# price_list('iphone', 2500)
# price_list('laptop', 1500)


# def price_list_2(**kwards): #ждут неогр колво проимен аргументов
#     print(kwards)
#     for product in kwards.items():
#         title, price = product
#         print(f'Product {title} price is {price}')

# price_list_2(iphone=2500, laptop=150, samsung=2000)