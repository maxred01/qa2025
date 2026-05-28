# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# try:
#     driver.get('https://kufar.by')
#     wait = WebDriverWait(driver, 10)
#
#     # 1. Закрываем куки
#     cookie_btn = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, '//div[contains(@class, "Modal_styles_overlay")]//button')
#     ))
#     cookie_btn.click()
#
#     # Пауза, чтобы окно гарантированно исчезло
#     time.sleep(1)
#
#     # 2. Кликаем по первой категории в списке
#     # Ищем ссылки (a), которые находятся внутри кнопок категорий (category-chip)
#     category_link = wait.until(EC.element_to_be_clickable(
#         (By.CSS_SELECTOR, 'button[data-name="category-chip"] a, a[href*="/l/"]')
#     ))
#     category_link.click()
#
#     # Ждем загрузки новой страницы
#     time.sleep(4)
#
# finally:
#     driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')
driver.maximize_window()

driver.find_element(By.ID, "userName").send_keys('Egor1')
driver.find_element(By.ID, "userEmail").send_keys('Egor@egor.com')
driver.find_element(By.ID, "currentAddress").send_keys('Egor3')
driver.find_element(By.ID, "permanentAddress").send_keys('Egor4')

result_name = driver.find_element(By.ID, 'name').text
assert result_name.find('test') != -1, "не Egor1"

time.sleep(3)
driver.find_element(By.ID, "submit").click()
time.sleep(5)

print(driver.find_element(By.ID, 'name').text)



driver.quit()