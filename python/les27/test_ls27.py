from playwright.sync_api import Page, expect, BrowserContext, Dialog
from time import sleep
import re



# #проверка видимости
# def test_visible(page: Page):
#     page.goto('https://www.qa-practice.com/elements/input/simple')
#     reqs = page.locator('#req_text') #обьявление перем. элемента
#     expect(reqs).not_to_be_visible() # проверка не видимости элемент
#     expect(reqs).to_be_hidden() # тоже проверка не видимости элемента
#     page.locator('#req_header').click() # нажатие для открытия элемн
#     expect(reqs).to_be_visible() # проверка видимости элем
    


# работа со встроенным (браузерным) списком
# def test_enabled_and_selected(page:Page):
#     page.goto('https://www.qa-practice.com/elements/button/disabled')
#     button = page.locator('#submit-id-submit')
#     expect(button).to_be_disabled() # проверка что кнопка выкл
#     page.locator('#id_select_state').select_option('Enabled') #переключен списка
#     expect(button).to_be_enabled()
#     # expect(button, 'ITS EXPECT ENABLED').to_be_disabled() #если ошибка сообщит текст
#     expect(button).to_have_text('Submit') #проверяет что в кнопке такой текст
#     expect(button).to_contain_text('ubm') # проверяет что в кнопке содержит такой текст
    
    
# # поиск текста в строке
# def test_value(page:Page):
#     text = 'qwert'
#     page.goto('https://www.qa-practice.com/elements/input/simple')
#     input_firld = page.locator('#id_text_string')
#     input_firld.fill(text)
#     expect(input_firld, f'input value is not {text}').to_have_value(text)
    
    


# def test_sort_and_waits(page:Page):
#     page.goto('https://megamarket.ru/catalog/nabory-posudy-8010105/')
#     # выберет 1 элемент из множества элементов (счет с 0)
#     first = page.locator('.ddl_product_link').locator('nth=0') 
#     print(first.inner_text())
#     sleep(4)
#     page.locator('#controls__btn').locator('nth=0').select_option('Новинки')
#     print(first.inner_text())    
#     sleep(4)


# # работа с вкладками tab
# def test_tabs(page:Page, context: BrowserContext):
#     page.goto('https://www.qa-practice.com/elements/new_tab/link')
#     link = page.locator('#new-page-link')
    
#     # вкл отслеживание появл новой страницы
#     with context.expect_page() as new_page_event:
#         link.click()
#     sleep(3)
#     new_page = new_page_event.value
#     result = new_page.locator('#result-text')
#     expect(result).to_have_text('I am a new page in a new tab')
#     page.get_by_role('link', name = 'New tab button').click()
#     sleep(3)


# #наведение
# def test_hover(page:Page):
#     page.goto('https://ultimateqa.com/automation')
#     first = page.get_by_text('Education') 
#     sleep(4)
#     first.hover()
#     second = page.get_by_text('Free Courses').locator('nth=0')
#     second.click()
#     sleep(4)
    


# #перетягивание
# def test_dnd(page:Page):
#     page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
#     drag_me = page.locator('#rect-draggable')
#     drag_here = page.locator('#rect-droppable')
#     drag_me.drag_to(drag_here)
#     sleep(4)
    

def test_alert(page:Page):
    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()
        
    def fill_and_accept(alert:Dialog):
        alert.accept('some text')
      
            
    page.on('dialog', lambda alert: alert.accept('another text')) #включение отслеживание диалога
    # page.on('dialog', fill_and_accept) #включение отслеживание диалога
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(5)
    