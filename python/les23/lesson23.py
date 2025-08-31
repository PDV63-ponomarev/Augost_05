# from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver import Keys


# options = Options()
# options.add_argument('start-maximized') # for this options open browser for full wind
# options.add_argument('--window-size=500,500') # for this options open browser for custom size
# options.add_experimental_option('detach', True) # особые настройки, в данном случе параметр не закрываться
# driver = webdriver.Chrome(options=options)


# driver = webdriver.Chrome()
# driver.maximize_window() # open for full window
# driver.set_window_size(500, 500) # install custom size


# driver.get('https://ya.ru/') # open website

# print(driver.title)
# print(driver.current_url)

# search_input = driver.find_element(By.NAME, 'text') # имя строки text
# search_input.send_keys('cat') # ввести в строку cat
# search_input.send_keys(Keys.ENTER)
# title = driver.title

# if 'cat — Яндекс: нашёлся' in title:
#     rezult = 'Correct'
# else:
#     rezult = 'Uncorrect'

# print('')
# print(rezult)
# print('')
# while driver.title != 'Dog':
#     print('CORRECT')
# if driver.title == 'cat — Яндекс: нашёлся 1 млн результатов':
#     print('Correct')

# sleep(3) # пауза для визуального просмотра. В практике не используется




####################################################



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    # sleep(3)
    



# def test_id_name(driver):

#     input_data = 'random'
#     driver.get('https://www.qa-practice.com/elements/input/simple')

#     # text_string = driver.find_element(By.ID, 'id_text_string')
#     text_string = driver.find_element(By.CLASS_NAME, 'textinput')
#     text_string.send_keys(input_data)
#     # text_string.submit() # форма принимается (Enter)
#     text_string.send_keys(Keys.ENTER)

#     result_text = driver.find_element(By.ID, 'result-text')
#     assert result_text.text == input_data



# def test_classname(driver):
     
#     input_data = 'random'
#     driver.get('https://www.qa-practice.com/elements/input/simple')

#     text_string = driver.find_element(By.NAME, 'text_string')
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)

#     result_text = driver.find_element(By.CLASS_NAME, 'result-text')
#     print(result_text.text)
#     print(result_text.get_attribute('innerText'))
#     assert result_text.text == input_data 



# def test_tagname(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'



# def test_link(driver):
#     driver.get('https://www.qa-practice.com')
#     contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'input') #поиск по частичному совпадению
#     contact_link.click()
#     assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'
     


# def test_css_selector(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     # text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
#     # text_string = driver.find_element(By.CSS_SELECTOR, '.form-control')
#     text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
#     text_string.send_keys('RANDOM')
#     # text_string.send_keys(Keys.ENTER)
#     print(text_string.value_of_css_property('border-color'))
    # assert text_string.get_attribute('placeholder') == 'Submit me'


# def test_xpath(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_string = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
#     text_string.send_keys('RANDOM')
#     text_string.send_keys(Keys.ENTER)