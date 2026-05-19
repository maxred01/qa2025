import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/text-box')

driver.find_element(By.ID, "userName").send_keys('test')
driver.find_element(By.ID, "userEmail").send_keys('test@test.com')
driver.find_element(By.ID, "currentAddress").send_keys('test')
driver.find_element(By.XPATH, "permanentAddress").send_keys('12352535')
driver.find_element(By.ID, "submit").click()

results_name = driver.find_element(By.ID, "name").text

assert results_name.find('test') == -1
time.sleep(2)

driver.quit()