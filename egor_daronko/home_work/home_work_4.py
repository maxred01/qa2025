import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/webtables')
time.sleep(2)

        # Начальное количество строк в таблице == 3
#================================================================
cur_elements = driver.find_elements(By.XPATH, "//tbody//tr")
assert len(cur_elements) == 3, 'количество строк в таблице не равно 3'
#================================================================

        # Добавление новой (4) строки с данными в таблицу
#================================================================
driver.find_element(By.ID, "addNewRecordButton").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys('firstname')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys('lastname')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys('test@email.com')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='age']").send_keys('19')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='salary']").send_keys('1200')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='department']").send_keys('department')
time.sleep(0.5)
driver.find_element(By.ID, "submit").click()
time.sleep(2)
#================================================================

        # Проверка, что 4 строка добавилась и длина списка == 4
#================================================================
next_elements = driver.find_elements(By.XPATH, "//tbody//tr")
assert len(next_elements) == 4, 'ошибка добавления строки в таблицу'
#================================================================

        # Редактирование добавленной 4 строки таблицы
        # Очищаем поля
#================================================================
driver.find_element(By.XPATH, "//span[@class='mr-2' and @id='edit-record-4']").click()
time.sleep(0.5)

listi = ["//*[@id='firstName']",
         "//*[@id='lastName']",
         "//*[@id='userEmail']",
         "//*[@id='age']",
         "//*[@id='salary']",
         "//*[@id='department']"
         ]

for xpath in listi:
    field = driver.find_element(By.XPATH, xpath)
    field.send_keys(Keys.CONTROL + "a")
    field.send_keys(Keys.DELETE)
    time.sleep(0.5)

        # Заполняем поля данными
driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys('test')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys('test2')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys('test@mail.com')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='age']").send_keys('20')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='salary']").send_keys('21')
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='department']").send_keys('22')
time.sleep(0.5)
driver.find_element(By.ID, "submit").click()
time.sleep(2)
#============================================================

        #Проверка данных в отредактированной строке
#============================================================
row_text = driver.find_element(By.XPATH, "//tbody//tr[4]").text

data = ['test',
        'test2',
        'test@mail.com',
        '20',
        '21',
        '22'
       ]

for cur_data in data:
    assert cur_data in row_text, f"{cur_data} отсутствует"
        # Удаление строки
#============================================================
driver.find_element(By.XPATH, "//span[@id='delete-record-4']").click()
time.sleep(2)
#============================================================

        # Проверка, что строка удалена
#============================================================
last_elements = driver.find_elements(By.XPATH, "//tbody//tr")
assert len(last_elements) == 3, 'Удаление строки не выполнено'
#============================================================
driver.quit()
