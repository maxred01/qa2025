# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
#
# def test_checkbox():
#     driver = webdriver.Chrome()
#
#     driver.get('https://demoqa.com/checkbox')
#
#     driver.find_element(By.XPATH, '//*[@id="root""]//*[@role="tree"]//span)[2]"').click()
#     driver.find_element(By.XPATH, '(//*[@aria-expanded="false"])[1]/*[2]').click()
#     check_box = driver.find_element(By.XPATH, '//*[@aria-label="Select Notes"]')
#     assert check_box.is_enabled()
#
#
#     time.sleep(2)
#
#     driver.quit()


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def test_checkbox():
#     driver = webdriver.Chrome()
#
#     driver.get('https://demoqa.com/radio-button')
#
#     driver.find_element(By.XPATH, '//*[@name="like"])[1]').click()
#     driver.find_element(By.XPATH, '//*[@name="like"])[2]').click()
#     check_box = driver.find_element(By.XPATH, '//p//span')
#     assert check_box.is_enabled()
#
#     time.sleep(5)
#
#     driver.quit()


import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkbox():
    text = ['Привет!',
        'Как дела?',
        'Я все проиграл!',
        'Тебе норм там сидится?',
        'Я проиграл жену!',
        'Ты служил?',
        'Ау!',
        'ку-ку',
    ]
    text_random = random.choice(text)

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://belbet.by/')

    driver.find_element(By.XPATH, '//button[contains(text(),"Принять")]').click()
    time.sleep(2)
    driver.find_element(By.ID, 'uw-main-button').click()
    time.sleep(2)

    driver.find_element(By.ID, 'uw-button-chat').click()
    time.sleep(10)

    for i in range(5):
        driver.find_element(By.XPATH, '//textarea[@placeholder="Введите текст"]').send_keys(text_random)
        for time_send in range(10, 15):
            driver.find_element(By.ID, 'uw-message-submit-button').click()

    time.sleep(2)
    driver.quit()

