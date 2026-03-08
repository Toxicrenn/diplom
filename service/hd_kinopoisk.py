from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
from config.config import BASE_URL

class KinopoiskHD():
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get(BASE_URL)
        sleep(5)

    def click_kinopoisk_hd(self) -> None:
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[data-tid="acc26a70"][href="https://hd.kinopoisk.ru/"]')
            )
        ).click()