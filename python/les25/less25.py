from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)
    
    

#прокрутка страницы 

#до конца вниз
# def test_scroll(driver):
#     driver.get('https://www.consultant.ru/')
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    

# до элемента
# def test_scroll_to_element(driver):
#     driver.get('https://the-internet.herokuapp.com/')
#     link = driver.find_element(By.LINK_TEXT, 'JQuery UI Menus')
#     driver.execute_script('arguments[0].scrollIntoView();', link)


#выбор для загрузки элемент
# def test_upload(driver):
#     driver.get('https://the-internet.herokuapp.com/upload')
#     upload = driver.find_element(By.ID, 'file-upload')
#     button = driver.find_element(By.ID, 'file-submit')
#     upload.send_keys('C:/Users/ponomarev.dv/Downloads/image.png')
#     sleep(3)
#     button.click()
    
    