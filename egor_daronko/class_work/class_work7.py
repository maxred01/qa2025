import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_buttons():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)

    driver.maximize_window()
    driver.get('https://demoqa.com/buttons')

    time.sleep(2)
    actions.double_click(driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')).perform()
    assert driver.find_element(By.ID, 'doubleClickMessage'), "doubleClickMessage не нажат"

    time.sleep(1)
    actions.context_click(driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')).perform()
    assert driver.find_element(By.ID, 'rightClickMessage'), "rightClickMessage не нажат"

    driver.find_element(By.XPATH, '//*[@id="item-5"]/a').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="simpleLink"]').click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/a[1]/div').click()
    time.sleep(3)

    assert driver.current_url == "https://demoqa.com/elements", 'ссылка не та'



    time.sleep(4)
    driver.quit()


