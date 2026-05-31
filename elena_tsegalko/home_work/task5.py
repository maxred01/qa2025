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
    element_firstName = driver.find_element(By.XPATH, f"//*[text()='{user['firstname']}']")
    element_lastName = driver.find_element(By.XPATH, f"//*[text()='{user['lastname']}']")

    assert element_firstName.text == user['firstname'], f"Пользователь {user['firstname']} {user['lastname']} не создан."
    assert element_lastName.text == user['lastname'], f"Пользователь {user['firstname']} {user['lastname']} не создан."
    time.sleep(2)

# редактирование формы
driver.find_element(By.ID, "edit-record-4").click()
time.sleep(2)
driver.find_element(By.ID, 'firstName').clear()
driver.find_element(By.ID, 'firstName').send_keys("Harry")
driver.find_element(By.ID, 'lastName').clear()
driver.find_element(By.ID, 'lastName').send_keys("Potter")
driver.find_element(By.ID, 'age').clear()
driver.find_element(By.ID, 'age').send_keys("12")
time.sleep(2)
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

element_firstName = driver.find_element(By.XPATH, f"//*[text()='{'Harry'}']")
element_lastName = driver.find_element(By.XPATH, f"//*[text()='{'Potter'}']")
element_age = driver.find_element(By.XPATH, f"//*[text()='{12}']")

assert element_firstName.text == "Harry", f"Имя пользователя не изменилось"
assert element_lastName.text == "Potter", f"Фамилия пользователя не изменилась"
assert int(element_age.text) == 12, f"Возраст пользователя не изменился"
time.sleep(2)


#Удаление формы
button = driver.find_element(By.ID, "delete-record-5")
ActionChains(driver).move_to_element(button).click().perform()

rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
count = len(rows)

assert count == 4, "Ошибка удаления строк"


time.sleep(2)
driver.quit()
