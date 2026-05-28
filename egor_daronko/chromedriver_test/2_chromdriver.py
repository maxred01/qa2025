import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.21vek.by/?utm_source=google&utm_medium=cpc&utm_campaign=336837170&utm_content=20888055050|596687804571&utm_term=21%20dtr&gad_source=1&gad_campaignid=336837170&gclid=EAIaIQobChMIgqmPxZLalAMVrgqiAx1E5wqPEAAYASAAEgJmQfD_BwE")

time.sleep(5)
try:
    driver.find_element(By.XPATH, '//*[@id="modal-cookie"]/div/div[2]/div[2]/button[1]/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="modal"]/div/div/div/div[2]/button[1]/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/button/div').click()
except:
    pass
time.sleep(5)
driver.find_element(By.ID, 'catalogSearch').click()
time.sleep(5)
driver.find_element(By.ID, 'catalogSearch').send_keys("test")
time.sleep(5)