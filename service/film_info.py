from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
from config.config import BASE_URL

class FilmInfo:
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get(BASE_URL + "/film/6039/")
        sleep(2)
    
    def get_film_info(self) -> dict:
        year = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-tid='cfbe5a01']")
            )
        ).text
        name = self._driver.find_element(By.CSS_SELECTOR,"[data-tid='75209b22']").text

        film_info = {
           'year': year,
           'name': name
        }
        return film_info

    