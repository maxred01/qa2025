import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from aliona_shaban.conftest import driver

def test_checkbox(driver):
    time1 = [10, 11, 12, 13, 14, 15]
    text = ['Привет!',
        'Как дела?',
        'Я все проиграл!',
        'Тебе норм там сидится?',
        'Я проиграл жену!',
        'Ты служил?',
        'Ау!',
        'ку-ку',
    ]

    time_random = random.choice(time1)


    driver.get('https://belbet.by/')

    driver.find_element(By.XPATH, '//button[contains(text(),"Принять")]').click()

    driver.find_element(By.ID, 'uw-main-button').click()


    driver.find_element(By.ID, 'uw-button-chat').click()


    for i in range(5):
        text_random = random.choice(text)
        driver.find_element(By.XPATH, '//textarea[@placeholder="Введите текст"]').send_keys(text_random)
        time.sleep(time_random)
        driver.find_element(By.ID, 'uw-message-submit-button').click()

    time.sleep(time_random)


