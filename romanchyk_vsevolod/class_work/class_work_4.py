import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')

driver.find_element(By.ID, "userName").send_keys('Ado')
driver.find_element(By.ID, "userEmail").send_keys('ado@adorable.com')
driver.find_element(By.ID, "currentAddress").send_keys('adorable')
driver.find_element(By.ID, "permanentAddress").send_keys('kasfj')
driver.find_element(By.ID, "submit").click()


result_name = driver.find_element('name').test
assert result_name.find('name') != -1
print(driver.find_element('email'))
print(driver.find_element('currentAddress'))
print(driver.find_element('permanentAddress'))


time.sleep(3)

driver.quit()
