import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#проверка наличия иконки википедии
wiki_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-icon')
time.sleep(2)
assert wiki_icon.is_displayed(), "Иконка Wikipedia не найдена"

#наличие поля ввода по айди
pole_vvoda = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
assert pole_vvoda.is_displayed(), "поле ввода не найдено"

#поиск википедии по классу
wiki_class = driver.find_element(By.CLASS_NAME, "wikipedia-search-input")
assert wiki_class.is_displayed(), "википедия не найдена"

#<h2 class="title">Tabs</h2>
some_elements = driver.find_elements(By.TAG_NAME, "h2")[5]
assert some_elements.is_displayed(), "элемент тэга h2 отсутствует"
print(some_elements.text)

