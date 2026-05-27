import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/webtables')

    driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]').click()
    driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').send_keys('test')
    driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('tester')
    driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('test@gmail.com')
    driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').send_keys('33')
    driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').send_keys('10000')
    driver.find_element(By.XPATH, '//*[@placeholder="Department"]').send_keys('test')
    submit = driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button)[2]')
    submit.click()

    driver.find_element(By.XPATH, '(//*[@data-toggle="tooltip"])[7]//*[@stroke="currentColor"]').click()

    driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').send_keys('alexei')

    driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('do')

    driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('popins@gmail.com')

    driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').clear()
    driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').send_keys('67')

    driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').send_keys('6767676767')

    driver.find_element(By.XPATH, '//*[@placeholder="Department"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="Department"]').send_keys('folks')


    submit_updated = driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button)[2]')
    submit_updated.click()
    assert submit_updated.is_enabled()

    time.sleep(3)

    driver.find_element(By.XPATH, '(//*[@data-toggle="tooltip"])[8]//*[@stroke="currentColor"]').click()

    time.sleep(3)

    driver.quit()


def test_webtables_add():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://demoqa.com/webtables')

    driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]').click()
    driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').send_keys('test')
    driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('tester')
    driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('test@gmail.com')
    driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').send_keys('33')
    driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').send_keys('10000')
    driver.find_element(By.XPATH, '//*[@placeholder="Department"]').send_keys('test')
    submit = driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button)[2]')
    submit.click()

    assert submit.is_enabled()
    assert driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('tester')
    assert driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('test@gmail.com')
    assert driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').send_keys('33')
    assert driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').send_keys('10000')
    assert driver.find_element(By.XPATH, '//*[@placeholder="Department"]').send_keys('test')

    time.sleep(3)

    driver.quit()


def test_webtables_update():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://demoqa.com/webtables')


    driver.find_element(By.XPATH, '(//*[@data-toggle="tooltip"])[5]//*[@stroke="currentColor"]').click()

    driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').send_keys('alexei')

    driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('do')

    driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('popins@gmail.com')

    driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').clear()
    driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').send_keys('67')

    driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').send_keys('6767676767')

    driver.find_element(By.XPATH, '//*[@placeholder="Department"]').clear()
    driver.find_element(By.XPATH, '//*[@placeholder="Department"]').send_keys('folks')

    submit_updated = driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button)[2]')
    submit_updated.click()

    assert submit_updated.is_enabled()
    assert driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').send_keys('alexei')
    assert driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('do')
    assert driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('popins@gmail.com')
    assert driver.find_element(By.XPATH, '// *[ @ placeholder = "Age"]').send_keys('67')
    assert driver.find_element(By.XPATH, '//*[@placeholder="Salary"]').send_keys('6767676767')
    assert driver.find_element(By.XPATH, '//*[@placeholder="Department"]').send_keys('folks')

    time.sleep(3)

    driver.quit()


def test_webtables_delete():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://demoqa.com/webtables')

    driver.find_element(By.XPATH, '(//*[@data-toggle="tooltip"])[6]//*[@stroke="currentColor"]').click()

    assert driver.find_element(By.XPATH, '(//*[@data-toggle="tooltip"])[6]//*[@stroke="currentColor"]').is_displayed()

    time.sleep(3)

    driver.quit()
