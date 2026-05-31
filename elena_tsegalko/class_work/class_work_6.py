import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# def test_buttons():
#     driver = webdriver.Chrome()
#     actions = ActionChains(driver)
#
#     driver.maximize_window()
#     driver.get("https://demoqa.com/buttons")
#
#     time.sleep(2)
#     actions.double_click(driver.find_element(By.ID, "doubleClickBtn")).perform()
#     assert driver.find_element(By.ID, "doubleClickMessage"), "Сообщение о двойном нажатии не появилось"
#     time.sleep(2)
#     actions.context_click(driver.find_element(By.ID, "rightClickBtn")).perform()
#
#     time.sleep(2)
#
#     # double_message = driver.find_element(By.ID, "doubleClickMessage").text
#     # right_message = driver.find_element(By.ID, "rightClickMessage").text
#
#
#     driver.quit()
#
#     # assert double_message == "You have done a double click"
#     # assert right_message == "You have done a right click"

def test_links():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://demoqa.com/links")

    driver.find_element(By.ID, "simpleLink").click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://demoqa.com/"
    time.sleep(2)

    driver.quit()
