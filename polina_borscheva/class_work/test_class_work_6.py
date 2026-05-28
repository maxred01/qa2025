import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from polina_borscheva.conftest import driver


def test_checkbox(driver):

    driver.get('https://demoqa.com/checkbox')

    driver.find_element(By.XPATH, '//*[@aria-expanded="false"]/*[2]').click()
    driver.find_element(By.XPATH, '(// *[@ aria-expanded="false"])[1] / * [2]').click()
    checkbox = driver.find_element(By.XPATH, '//*[@aria-label="Select Notes"]')
    checkbox.click()

    assert checkbox.is_enabled()
    time.sleep(3)



def test_radio_button():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://demoqa.com/radio-button')

    driver.find_element(By.XPATH, '(//*[@name="like"])[1]').click()
    yes_massage = driver.find_element(By.XPATH, '(//*[@id="root"]//div)[49]//p//span')
    yes_massage.click()

    assert yes_massage
    time.sleep(3)

    driver.quit() 