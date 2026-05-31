import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#XPATH локаторы страницы https://hyperskill.org/courses
driver.get("https://hyperskill.org/courses")
time.sleep(4)
driver.find_element(By.XPATH, '//body//a[@class ="absolute inset-0"]').click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.find_element(By.XPATH, '//span[text()=" Sign in "]').click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.find_element(By.XPATH, '//span[text()=" Start for free "]').click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.find_element(By.XPATH, '//a[@data-component-name="BLink"]').click()
time.sleep(4)
driver.get("https://hyperskill.org/courses")
time.sleep(4)
driver.find_element(By.XPATH, '//nav//li[@class="nav-item !mr-4"]').click()
time.sleep(4)
driver.find_element(By.XPATH, '//a[@class="nav-link dropdown-toggle flex items-center"]').click()
time.sleep(4)
driver.find_element(By.XPATH, '//section//a[@click-event-target="Python"]').click()
time.sleep(4)
