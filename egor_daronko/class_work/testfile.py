import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get('https://demoqa.com/webtables')
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='firstName']"))).send_keys('firstname')
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lastName']"))).send_keys('lastname')
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='userEmail']"))).send_keys('test@email.com')
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='age']"))).send_keys('19')
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='salary']"))).send_keys('1200')
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='department']"))).send_keys('department')
time.sleep(1)


wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
time.sleep(3)




driver.quit()
