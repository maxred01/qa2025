import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/text-box')

# driver.find_element(By.XPATH, "(//button[contains(text(),'Click Me')])[3]").click()
driver.find_element(By.ID, 'userName').send_keys('test')
driver.find_element(By.ID, 'userEmail').send_keys('test@t.com')
driver.find_element(By.ID, 'currentAddress').send_keys('find')
driver.find_element(By.ID, 'permanentAddress').send_keys('kjhhkljlj')
driver.find_element(By.ID, 'submit').click()

print(driver.find_element(By.ID, 'name').text)

results_name = driver.find_element(By.ID, 'name').text

assert results_name.find( 'test') != -1
time.sleep(3)

driver.quit()
