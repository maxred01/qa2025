import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
users = [
    {
        "firstname": "Vasya",
        "lastname": "Vaskov",
        "userEmail": "Vaskov@test.ru",
        "age": 24,
        "salary" : 2800,
        "department": "QA"
    },
    {
        "firstname": "Petya",
        "lastname": "Petrov",
        "userEmail": "Petrov@test.ru",
        "age": 30,
        "salary" : 5000,
        "department": "DevOps"
    }
]
# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()
driver.maximize_window()
# Открыть страницу
driver.get("https://demoqa.com/webtables")
time.sleep(2)

for user in users:
    driver.find_element(By.ID, 'addNewRecordButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'firstName').send_keys(user["firstname"])
    driver.find_element(By.ID, 'lastName').send_keys(user["lastname"])
    driver.find_element(By.ID, 'userEmail').send_keys(user["userEmail"])
    driver.find_element(By.ID, 'age').send_keys(user["age"])
    driver.find_element(By.ID, 'salary').send_keys(user["salary"])
    driver.find_element(By.ID, 'department').send_keys(user["department"])
    driver.find_element(By.ID, 'submit').click()
    time.sleep(2)
    element_firstName = driver.find_element(By.XPATH, f"//*[text()='{user["firstname"]}']")
    element_lastName = driver.find_element(By.XPATH, f"//*[text()='{user["lastname"]}']")

    assert element_firstName.text == user["firstname"], f"Пользователь {user["firstname"]} {user["lastname"]} не создан."
    assert element_lastName.text == user["lastname"], f"Пользователь {user["firstname"]} {user["lastname"]} не создан."
    time.sleep(2)




#test delete
# buttons_to_click = ["delete-record-5", "delete-record-4"]
#
# for button_id in buttons_to_click:
#
#     button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, button_id))
#     )
#     button.click()
button = driver.find_element(By.ID, "delete-record-5")
ActionChains(driver).move_to_element(button).click().perform()


time.sleep(2)
driver.quit()
