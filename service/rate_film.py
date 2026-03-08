from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver

class FilmRating():
    def __init__(self, browser:WebDriver) -> None:
        """Заходит на сайт"""
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/film/6290547/")
        
    sleep(4)

    def click_rate(self) -> None:
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-tid="410c06ef"]')
            )
        ).click()

    def film_rate(self) -> None:
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[aria-label="Оценка 9"]')
            )
        ).click()
      
    
    

    



