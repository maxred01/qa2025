import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# def test_button():
#     driver = webdriver.Chrome()
#     actions = ActionChains(driver)
#     driver.maximize_window()
#     driver.get('https://demoqa.com/buttons')
#
#     time.sleep(2)
#     actions.double_click(driver.find_element(By.ID, 'doubleClickBtn')).perform()
#     time.sleep(2)
#     actions.context_click(driver.find_element(By.ID, 'rightClickBtn')).perform()
#
#     assert driver.find_element(By.ID, 'doubleClickMessage'), 'Сообщение о двойном нажатии не появилось'
#     assert driver.find_element(By.ID, 'rightClickMessage'), 'Сообщение о правом нажатии не появилось'
#
#
#
#     time.sleep(2)
#     driver.quit()

    # driver.find_element(By.ID, '//*[@id="doubleClickBtn"]').click()
    # driver.find_element(By.ID, '//*[@id="doubleClickBtn"]').click()

def test_links():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    driver.maximize_window()
    driver.get('https://demoqa.com/links')

    driver.find_element(By.XPATH, '//*[@id="simpleLink"]').click()
    time.sleep(2)

    print(driver.current_url)

    driver.switch_to.window(driver.window_handles[1])

    print(driver.current_url)


    assert driver.current_url == "https://demoqa.com/"

    time.sleep(5)
    driver.quit()