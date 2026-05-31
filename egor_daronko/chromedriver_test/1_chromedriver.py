import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://people.andersenlab.com/")
driver_title = driver.title
print(driver_title)
time.sleep(5)

driver.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
new_driver_title = driver.title
print(new_driver_title)
time.sleep(5)

driver.back()
assert "people.andersenlab.com" in driver.current_url
time.sleep(5)

driver.refresh()
time.sleep(5)
new_driver_url = driver.current_url
print(new_driver_url)

driver.forward()
time.sleep(5)
assert "wikipedia.org" in driver.current_url
time.sleep(5)



