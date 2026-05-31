import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_webtable():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/webtables')

    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]').click()
    driver.find_element(By.XPATH, '//*[@aria-modal="true"]//*[@id="firstName-wrapper"]//input').send_keys('test')
    driver.find_element(By.XPATH, '//*[@id="lastName-wrapper"]//input').send_keys('test_test')
    driver.find_element(By.XPATH, '// *[ @ id = "userEmail-wrapper"] // input').send_keys('test@test.by')
    driver.find_element(By.XPATH, '//*[@id="age-wrapper"]//input').send_keys('25')
    driver.find_element(By.XPATH, '//*[@id="salary-wrapper"]//input').send_keys('5400')
    driver.find_element(By.XPATH, '//*[@id="department-wrapper"]//input').send_keys('legal')
    driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button)[2]').click()
    elements = driver.find_element(By.XPATH, )


# assert len(driver.find_element() == 3
# results_name = driver.find_element(By.XPATH, '(//*[@id="root"]//td)[1]').text
# assert results_name.find( 'test') != -1
time.sleep(5)
# driver.quit()

