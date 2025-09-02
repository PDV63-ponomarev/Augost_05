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
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    sleep(3)


# def test_new_tab(driver):
#     driver.get('https://www.qa-practice.com/elements/new_tab/link')
#     sleep(3)
#     driver.find_element(By.ID,'new-page-link').click()
#     tabs=driver.window_handles #выбор вкладки
#     driver.switch_to.window(tabs[1]) #переключится на 2 вкладку
#     result = driver.find_element(By.ID, 'result-text')
#     assert result.text == 'I am a new page in a new tab'
#     driver.close() # закрывает вкладку
#     driver.switch_to.window(tabs[0]) # перекключается обратно на 1 вкладку
    

###############################


# поиск элемента на встроенной странице iframe

def test_iframe(driver):
    
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME,'iframe')
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME,'navbar-toggler-icon')
    burger_menu.click()
    sleep(2)
    driver.switch_to.default_content() #выйтий из iframe
    driver.find_element(By.LINK_TEXT, 'Iframe')


###############################

# при поиске и исп элемента, селениум запомнает его индекс
# индекс элемента обнуляется при обновлении или измменении страницы
# поиск нужно возобновлять даже если визуальных изменений страницы нету

# def test_ctale_excep(driver):
#     driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
#     sleep(3)
#     checkbox = driver.find_element(By.ID, 'id_checkbox_0')
#     checkbox.click()
#     submit = driver.find_element(By.ID,'submit-id-submit')
#     submit.click()
#     assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
#     checkbox = driver.find_element(By.ID, 'id_checkbox_0')
#     checkbox.click()
#     submit = driver.find_element(By.ID,'submit-id-submit')
#     submit.click()