import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkbox():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/checkbox')

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@aria-expanded="false"]/*[2]').click()
    driver.find_element(By.XPATH, '(//*[@aria-expanded="false"])[1]/*[2]').click()
    check_box = driver.find_element(By.XPATH, '//*[@aria-label="Select Notes"]')
#
#
    check_box.click()
# #
# # assert check_box.is_enabled()

    def test_checkbox():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://demoqa.com/radio-button')

    check_box = driver.find_element(By.XPATH, '(//*[@name="like"])[1]').click()

    from select import select
    # assert check_box.select()
    time.sleep(5)
    driver.quit()