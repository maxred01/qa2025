# import time
# from lib2to3.pgen2 import driver
#
# from selenium import webdriver
# from selenium.webdriver.common import actions
# from selenium.webdriver.common.by import By
#
#
# def test_buttons():
#
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     driver.get('https://demoqa.com/buttons')
#
#     time.sleep(2)
#     actions.double_click(By.ID, 'doubleClickBtn').perform()
#     assert driver.find_element(By.ID, 'doubleClickMessage'), 'Сообщение с дабл кликом'
#
#     time.sleep(2)
#     actions.context_click(By.ID, 'rightClickBtn').perform()
#     assert driver.find_element(By.ID, 'rightClickMessage'), 'Сообщение с правым кликом'
#
#
#     time.sleep(10)
#     driver.find_element(By.ID, 'IOP4h').click()


import time

from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from romanchyk_vsevolod.conftest import driver


def test_buttons():

    driver.get('https://demoqa.com/links')

    driver.find_element(By.ID, 'simpleLink').click()
    driver.switch_to.window(driver.window_handles[1])


