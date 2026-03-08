from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class KinopoiskHD():
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru")
    
    sleep(5)

    def click_kinopoisk_hd(self) -> None:
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[data-tid="acc26a70"][href="https://hd.kinopoisk.ru/"]')
            )
        ).click()