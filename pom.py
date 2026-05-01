from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class KodillaStorePom:

    def __init__(self, driver):
        self.driver = driver

    @property
    def search_bar(self):
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchField"))
    )

    @property
    def search_results(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".element"))
            )
        except TimeoutException:
            return []
        
    def search(self, text):
        search_input = self.search_bar
        search_input.clear()
        search_input.send_keys(text)

        return self.search_results