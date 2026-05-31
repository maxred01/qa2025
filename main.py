import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablesTests(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/webtables")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_add_record(self):
        driver = self.driver


        initial_rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        initial_count = len(initial_rows)

        add_button = driver.find_element(By.ID, "addNewRecordButton")
        add_button.click()


        self.wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Иван")
        driver.find_element(By.ID, "lastName").send_keys("Петров")
        driver.find_element(By.ID, "userEmail").send_keys("ivan.petrov@example.com")
        driver.find_element(By.ID, "age").send_keys("30")
        driver.find_element(By.ID, "salary").send_keys("50000")
        driver.find_element(By.ID, "department").send_keys("IT")


        driver.find_element(By.ID, "submit").click()


        self.wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")) == initial_count + 1)
        new_rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        self.assertEqual(len(new_rows), initial_count + 1)


        last_row = new_rows[-1]
        cells = last_row.find_elements(By.CSS_SELECTOR, ".rt-td")
        self.assertIn("Иван", cells[0].text)
        self.assertIn("Петров", cells[1].text)
        self.assertIn("ivan.petrov@example.com", cells[2].text)

    def test_edit_record(self):
        driver = self.driver


        first_row = driver.find_element(By.CSS_SELECTOR, ".rt-tr-group")
        edit_button = first_row.find_element(By.CSS_SELECTOR, "[title='Edit']")
        edit_button.click()


        first_name_input = self.wait.until(EC.visibility_of_element_located((By.ID, "firstName")))


        first_name_input.clear()
        first_name_input.send_keys("Алексей")


        driver.find_element(By.ID, "submit").click()


        cells = first_row.find_elements(By.CSS_SELECTOR, ".rt-td")
        self.assertIn("Алексей", cells[0].text)

    def test_delete_record(self):
        driver = self.driver


        initial_rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        initial_count = len(initial_rows)
        if initial_count == 0:
            self.skipTest("Нет записей для удаления")


        first_row = initial_rows[0]
        delete_button = first_row.find_element(By.CSS_SELECTOR, "[title='Delete']")
        delete_button.click()


        self.wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")) == initial_count - 1)
        current_rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        self.assertEqual(len(current_rows), initial_count - 1)

if __name__ == "__main__":
    unittest.main()