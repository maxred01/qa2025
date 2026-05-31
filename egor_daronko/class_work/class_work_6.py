import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkbox(driver):
    text = ['Привет!',
        'Как дела?',
        'Я все проиграл!',
        'Тебе норм там сидится?',
        'Я проиграл жену!',
        'Ты служил?',
        'Ау!',
        'ку-ку',
    ]

    driver.get('https://belbet.by/')

    driver.find_element(By.XPATH, '//button[contains(text(),"Принять")]').click()
    driver.find_element(By.ID, 'uw-main-button').click()
    driver.find_element(By.ID, 'uw-button-chat').click()

    for _ in range(len(text)):
        driver.find_element(By.XPATH, '//textarea[@placeholder="Введите текст"]').send_keys(random.choice(text))
        time.sleep(random.randint(10, 15))
        driver.find_element(By.ID, 'uw-message-submit-button').click()

