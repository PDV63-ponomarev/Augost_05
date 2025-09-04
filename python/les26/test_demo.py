from playwright.sync_api import Page, expect
import re
from time import sleep

# для просмотра аргумент --headed
# pytest --headed


# def test_one(page: Page):
#     page.goto('https://www.google.com/') # go in google
#     search_fild = page.get_by_role('combobox') # find parametr stright
#     search_fild.fill('cat') # get text in stright
#     search_fild.press('Enter') 
#     # проверяет что титульник содержит cat
#     expect(page).to_have_title(re.compile('cat'))
#     sleep(2)
    
    # ^cat в начале строки
    # cat$  в конце строки
    # cat просто в строке
    
    
# def test_by_role(page: Page):
#     page.goto('https://magento.softwaretestingboard.com/')
#     page.get_by_role('menuitem', name = "Waht's New").click()
#     page.get_by_role('link', name = 'Search Terms').click()
    
    
        
#### поиск по элементу текста
# def test_by_text(page: Page):
#     page.goto('https://www.qa-practice.com/')
#     page.get_by_text('Single UI Elements').click()
#     sleep(2)
    
# def test_by_label(page: Page):
#     page.goto('https://www.qa-practice.com/elements/input/simple')
#     field = page.get_by_label('Text string')
#     sleep(3)
#     field.press_sequentially('TEXT', delay=500) #скорость набора текста
#     sleep(1)
#     field.press('Control+a')
#     sleep(1)
#     field.press('Backspace')
#     sleep(3)
    
    
# def test_by_placeholder(page: Page):
#     page.goto('https://www.qa-practice.com/elements/input/simple')
#     page.get_by_placeholder('Submit me').fill('TEST2')
#     sleep(2)
    
    
# # поиск по альтернативному тексту
# def test_by_alt_text(page: Page):
#     page.goto('https://ru.ruwiki.ru/wiki/EPAM_Systems')
#     page.get_by_alt_text('Изображение логотипа').click()
#     sleep(2)
    
    
# def test_by_title(page: Page):
#     page.goto('https://www.google.com/') 
#     page.get_by_title('Поиск').fill('cat')
#     sleep(2)
    

# поиск по тест id
# def test_by_testid(page: Page):
#     page.goto('https://www.airbnb.ru/')
#     page.get_by_test_id('tabBarItem-EXPERIENCES').click()
#     sleep(2)


# def test_by_locator(page: Page):
#     page.goto('https://1000-m.ru/')
#     page.locator('[title="Магазин 1000 мелочей"]').click()
#     sleep(2)


# def test_by_xpath(page:Page):
#     page.goto('https://blog.qiwi.com/')
#     page.locator('//*[@data-original="images/tild3038-3336-4633-b562-616462663930__17.png"]').click()

