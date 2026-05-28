import time
import random
from selenium.webdriver.common.by import By
from maksim_tsybulka.conftest import driver


def test_checkbox(driver):

    driver.get('https://dzen.ru/')
    driver.find_element(By.XPATH, "//*[@class='dzen-layout--navigation-tab__text-2g' and contains(text(),'Найти')]").click()
    driver.find_element(By.ID, "search-input").send_keys('halibut testing')
    driver.find_element(By.XPATH, '//*[@class=" dzen-layout--base-button__childrenContent-1L" and contains(text(),"Найти")]').click()
    driver.find_element(By.XPATH, '(//a[@class="search--base-tab__tab-3s search--default-tab__rootElement-iZ search--base-button__rootElement-12  search--base-button__l-2a  search--base-button__tab-10"])[3]').click()
    driver.find_element(By.XPATH, '(//a[@aria-label="Название канала"])[1]').click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, "//div[contains(text(),'СОЗДАЕМ TELEGRAM-БОТ ДЛЯ ПРОВЕРКИ ССЫЛОК НА СТРАНИЦЕ')]").click()
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    time.sleep(2)
