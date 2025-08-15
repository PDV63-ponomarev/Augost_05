def calc (x, y):
    try: #проверка на ошибки. обработчик ошибок
        return x / y
    except ZeroDivisionError as err: # если конкретная ошибка то будет это
        print('Na 0 delete nelza')
        print(err)
   
    except: # если какая либо другая ошибка
        print('Some error')

print(calc(5, 0))
# print(calc(4, 'fds'))
print('hello')