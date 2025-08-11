# Распаковка
# когда знаем сколько элементов в массиве-листе, коллекции
# можно распределить элементы коллекции по переменным


# my_list = [1, 3]
# my_tuple = (4, 6, 7)

# a = my_list[0]
# b = my_list[1]
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]

# a, b = my_list
# c, d, e = my_tuple

# print(a, b, c, d, e)

# Обращение к элементу по индексу считается не очень хорошо




################################################################

# Срез
# позволяет из списка взять определенную его часть

# srez = [1, 3, 4, 5, 6, 7, 8, 9]
# print(srez)
# print(srez[0:4]) # от 0 включительно, до 4 не включительн
# print(srez[2:5]) # от 2 включительно, до 5 не включительн
# print(srez[:3]) # с начала и до 3 инд не включительно
# print(srez[4:]) # от 4 включительно и до конца
# print(srez[1::2]) # от 1 индекса, до конца, каждый 2 элемент
# print(srez[::3]) # c начала и до конца каждый 3 элемент
# print(srez[::-1]) # печатает с конца и до начала
# print(srez[::-2]) # печатает с конца и до начала каждый 2 элемент
# print(srez[-2:-7:-1])



################################################################

# Методы строк
# по сути строка это кортеж символов со строго занятой последовательностью

# text = "my Longs Long story"
# print(text[3]) # индекс символа в строке 
# print(len(text)) #количество символов
# print(text.index("s")) #позиция символа 
# print(text.index("Long "))# позиция слова, в случае не нахождения ошибка
# print('Long' in text) #есть ли слово 
# print(text.count('o')) # количество выбранных букв в тексте
# print(text.find('long')) #позиция слова. в случае не нахождения возврашает -1
# print(text[::2])
# print(text[::-1])
# print(text.startswith('my')) #если текст начинается с этого слова то True
# print(text.endswith('story')) #если текст заканчивается на это то true


# txt = 'ThIs tExt wiTH MeSsEd up CaPItaliZaTioN!'
# print(txt.capitalize()) #первая буква предложения заглавной
# print(txt.title()) #делает каждую первую букву большой
# print(txt.upper()) #делает все буквы большими
# print(txt.lower()) #делает все буквы маленькими
# txt2 = txt.lower()
# str_ind = txt.lower().index('text')
# str_ind2 = txt2.index(' with')

# print(txt2[:str_ind] + txt2[str_ind:str_ind2].upper() + txt2[str_ind2:])


# msg = '  Hello world!  '
# print(msg.replace('world', 'Dima')) #изменение слова на другое, но не меняет оригинал
# print(msg) #оригинал не изменен
# msg = msg.replace('world', 'Dima') #перезапись
# print(msg)
# print(msg.replace(' Dima', ''))
# print(msg.strip()) #удаляет пробелы по краям
# print(msg.lstrip())
# print(msg.rstrip())

# text = '"text"'
# print(text)
# text = text.strip('"') #удаляет ковычки по краям
# print(text)



################################################################

# Строка <--> Список

# my_string = 'some little text'
# list_from_text = my_string.split() #разбивает строку на массив по пробелами
# print(list_from_text)
# my_string2 = 'some-little-text'
# print(my_string2.split('-')) #разбивает строку на массив по выбр символу

# lang = ['Python', 'Java', 'Ruby']
# print(lang)
# lang2 = ', '.join(lang) #массив в строку с разделителем запятой
# print(lang2)
# print('Student knowd these language:', ', '.join(lang) )



################################################################

# Форматирование строки

# a = 'ONE'
# b = 'TWO'

# print('First word is', a, ', second word is', b) # не красиво, лишнии пробелы

# text = 'First word is ' + a + ', second word is ' + b #не рекоменд способ
# print(text) 

# text2 = 'First word is %s, second word is %s' #шаблон с подстановкой. Устарел
# print(text2 % (a, b)) #подставляется по порядку

# text3 = 'First word is {}, second word is {}' #шаблон с подстановкой.Не рекоменд
# print(text3.format(a, b)) #подставляется по порядку

# text4 = 'First word is {0}, second word is {1}' #шаблон с подстановкой.Рекоменд
# print(text4.format(a, b)) #подставляется по порядкуУправляемая подстановка

# text5 = 'First word is {1}, second word is {0}' #шаблон с подстановкой.Рекоменд
# print(text5.format(a, b)) #подставляется по порядку. Управляемая подстановка


# # f-string  Не подходит дя шаблона. Сначала переменные, потом текст
# my_text = f'First word is {a}, second word is {b}'
# print(my_text)


# template = 'Hello {0}!' #Можно исп для шаблона
# username = input('What is your name?')
# print(template.format(username))