from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from selenium.
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(6) #сколько времени искать элемент
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_clear(driver):
    driver: webdriver.Chrome
    input_data = 'random'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CLASS_NAME, 'textinput')
    text_string.send_keys(input_data)
    sleep(2)
    print(text_string.get_attribute('value')) #распечатает содержимое строки
    entere_value = text_string.get_attribute('value')
    
    # очистка поля
    # text_string.clear() 
    #
    for _ in range(len(entere_value)):
        text_string.send_keys(Keys.BACKSPACE)

    assert text_string.is_displayed()


############
# взаимодействие с переключателем

def test_enabled_and_select(driver):
   driver.get('https://www.qa-practice.com/elements/button/disabled')
   button = driver.find_element(By.NAME, 'submit')
   print(button.is_enabled())
   select = driver.find_element(By.ID,'id_select_state')
   dropdown = Select(select)
   dropdown.select_by_value('enabled')
   print(button.is_enabled())


#################
# timeout

def test_5_sec(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID,'visibleAfter')
    button3.click()
