кладки
    driver.switch_to.window(tabs[1]) #переключится на 2 вкладку
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'