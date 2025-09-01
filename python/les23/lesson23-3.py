from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(5) #сколько времени искать элемент
    chrome_driver.maximize_window()
    yield chrome_driver
    # sleep(3)


# def test_clear(driver):
#     driver: webdriver.Chrome
#     input_data = 'random'
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_string = driver.find_element(By.CLASS_NAME, 'textinput')
#     text_string.send_keys(input_data)
#     sleep(2)
#     print(text_string.get_attribute('value')) #распечатает содержимое строки
#     entere_value = text_string.get_attribute('value')
    
#     # очистка поля
#     # text_string.clear() 
#     #
#     for _ in range(len(entere_value)):
#         text_string.send_keys(Keys.BACKSPACE)

#     assert text_string.is_displayed()


############
# взаимодействие с переключателем

# def test_enabled_and_select(driver):
#    driver.get('https://www.qa-practice.com/elements/button/disabled')
#    button = driver.find_element(By.NAME, 'submit')
#    print(button.is_enabled())
#    select = driver.find_element(By.ID,'id_select_state')
#    dropdown = Select(select)
#    dropdown.select_by_value('enabled')
#    print(button.is_enabled())


#################
# timeout

# def test_5_sec(driver):
#     driver.get('https://demoqa.com/dynamic-properties')
#     button3 = driver.find_element(By.ID,'visibleAfter')
#     button3.click()



# def test_cart(driver):
#     driver.get('https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html')
#     size = driver.find_element(By.ID,'option-label-size-143-item-167').click()
#     color = driver.find_element(By.ID, 'option-label-color-93-item-50').click()
#     botton = driver.find_element(By.ID, 'product-addtocart-button').click()
#     wait = WebDriverWait(driver, 5) #ждать действия 5 секунд
#     wait.until_not( # ждать пока-не
#         EC.text_to_be_present_in_element_attribute( #ждет действия изменение 
#             (By.CSS_SELECTOR,'.counter.qty'), 
#             'class',
#             'empty'
#             )
#         )
#     wait = WebDriverWait(driver, 5) #ждать действия 5 секунд
#     wait.until_not( # ждать пока-не
#         EC.text_to_be_present_in_element_attribute( #ждет действия изменение 
#             (By.CSS_SELECTOR,'.counter.qty'), 
#             'class',
#             'loading'
#             )
#         )
#     counter = driver.find_element(By.CSS_SELECTOR, '.counter-number')
#     print(counter.text)



# def test_5_sec2(driver):
#     driver.get('https://demoqa.com/dynamic-properties')
#     # жди пока 5 секунд пока не появится такой элемент
#     WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'visibleAfter')))
#     button3 = driver.find_element(By.ID,'visibleAfter')
#     button3.click()
#     driver.add_cookie({'name': 'testname', 'value': 'testvelue'}) #подсовывает куки
#     print(driver.get_cookies())



###################
# поиск элемента среди повторяюшихся

# def test_same_elements(driver):
#     driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
#     sleep(4)
#     product_link = driver.find_elements(By.CLASS_NAME,'product-item-link')

#     print(product_link[0].text, '!!!!!!!!!')
#     print(product_link[-1].text, '222222')


    

def test_same_cards(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    sleep(5)
    product_link = driver.find_elements(By.CLASS_NAME,'product-item-info')
    for card in product_link:
        print(card.find_element(By.CLASS_NAME,'price').text)
    # print(product_link[0].find_element(By.CLASS_NAME,'price').text)
