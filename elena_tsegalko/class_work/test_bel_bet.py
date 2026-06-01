import time
import random
from selenium.webdriver.common.by import By
from elena_tsegalko.conftest import driver

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

    for i in range(5):
        driver.find_element(By.XPATH, '//textarea[@placeholder="Введите текст"]').send_keys(text[i])
        time.sleep(random.randint(5, 7))
        driver.find_element(By.ID, 'uw-message-submit-button').click()

    time.sleep(2)



