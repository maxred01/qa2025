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
    time.sleep(3)

    for i in range(5):
        driver.find_element(By.XPATH, '//textarea[@placeholder="Введите текст"]').send_keys(text_random)
        time.sleep(10)
        driver.find_element(By.ID, 'uw-message-submit-button').click()


    time.sleep(2)
    driver.quit()
