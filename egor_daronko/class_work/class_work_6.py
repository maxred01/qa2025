# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get('https://demoqa.com/checkbox')
#
# time.sleep(2)
# driver.find_element(By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), ' check-box-tree-wrapper ')]//*[@style='position: relative;']//*[@aria-expanded='false']/*[2]").click()
# time.sleep(2)
#
#
# time.sleep(2)
# # check_box = driver.find_element(By.XPATH, '//div[@class="rc-tree-treenode rc-tree-treenode-switcher-close rc-tree-treenode rc-tree-treenode-leaf"]//span[@role="checkbox"]')
# # check_box.click()
#
# # assert check_box.is_enabled()
# time.sleep(2)
# driver.quit()

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

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://belbet.by/')

    driver.find_element(By.XPATH, '//button[contains(text(),"Принять")]').click()
    time.sleep(2)
    driver.find_element(By.ID, 'uw-main-button').click()
    time.sleep(2)

    driver.find_element(By.ID, 'uw-button-chat').click()
    time.sleep(10)

    for _ in range(len(text)):
        driver.find_element(By.XPATH, '//textarea[@placeholder="Введите текст"]').send_keys(random.choice(text))
        time.sleep(random.randint(10, 15))
        driver.find_element(By.ID, 'uw-message-submit-button').click()

    time.sleep(2)
    driver.quit()