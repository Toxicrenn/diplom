from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


class AddToFolderFilm():
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get(BASE_URL + "/film/46708/")
        sleep(4)

    def click_add(self) -> None:
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[aria-label="Добавить в папку"]')
            )
        ).click()