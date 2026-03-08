from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

class DirectorInfo:
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/name/7640/")
        sleep(2)
    
    @allure.step('Получение информации о режиссере')   
    def get_director_info(self) -> dict:
        name_rus = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-tid='f22e0093']")
            )
        ).text
        name_eng = self._driver.find_element(By.CSS_SELECTOR,"[data-tid='7cdbd36a']").text

        director_info = {
           'name_rus': name_rus,
           'name_eng': name_eng
        }
        return director_info