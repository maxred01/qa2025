import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 1. Данные трех пользователей
users = [
    {"first": "Иван", "last": "Иванов", "email": "ivan@example.com", "age": "30", "salary": "50000", "dept": "IT"},
    {"first": "Анна", "last": "Петрова", "email": "anna@example.com", "age": "25", "salary": "60000", "dept": "HR"},
    {"first": "Петр", "last": "Сидоров", "email": "petr@example.com", "age": "35", "salary": "75000", "dept": "QA"}
]

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # 2. Цикл для последовательного добавления каждого пользователя
    for user in users:
        # Нажатие кнопки "Add"
        add_button = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        add_button.click()

        # Ожидание модального окна
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

        # Заполнение полей текущими данными из цикла
        driver.find_element(By.ID, "firstName").send_keys(user["first"])
        driver.find_element(By.ID, "lastName").send_keys(user["last"])
        driver.find_element(By.ID, "userEmail").send_keys(user["email"])
        driver.find_element(By.ID, "age").send_keys(user["age"])
        driver.find_element(By.ID, "salary").send_keys(user["salary"])
        driver.find_element(By.ID, "department").send_keys(user["dept"])

        # Нажатие кнопки "Submit"
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Небольшая пауза между добавлениями для стабильности
        time.sleep(1)

    # Итоговая пауза для проверки таблицы
    time.sleep(5)

finally:
    driver.quit()