import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_buttons():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)

    driver.maximize_window()
    driver.get('https://demoqa.com/buttons')

    time.sleep(2)
    actions.double_click(driver.find_element(By.ID, 'doubleClickBtn')).perform()
    time.sleep(2)
    actions.context_click(driver.find_element(By.ID, 'rightClickBtn')).perform()

    assert driver.find_element(By.ID, 'doubleClickMessage')
    assert driver.find_element(By.ID, 'rightClickMessage')

    time.sleep(2)
    driver.quit()


def test_links():
    driver = webdriver.Chrome()
    # actions = ActionChains(driver)

    driver.maximize_window()
    driver.get('https://demoqa.com/links')

    time.sleep(2)
    driver.find_element(By.ID, 'simpleLink').click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)

    assert driver.current_url == 'https://demoqa.com/'

    time.sleep(2)
    driver.quit()
    +