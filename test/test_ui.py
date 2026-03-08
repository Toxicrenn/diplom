import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from service.film_info import FilmInfo
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from service.rate_film import FilmRating
from service.hd_kinopoisk import KinopoiskHD
from service.add_to_folder_without_login import AddToFolderFilm
from service.director_info import DirectorInfo
from config.config import executable_path

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.mark.ui
@allure.title("Получение информации о фильме")
@allure.story("Получение информации")
def test_film_info(browser):
    film_page = FilmInfo(browser)
    expected_info = {
        'year': '1994',
        'name': 'Маска (1994)'
    }
    sleep(10)
    with allure.step('Получение информации о фильме'):
        actual_info = film_page.get_film_info()
    with allure.step("Проверка всей информации о фильме"):
        assert actual_info == expected_info
    with allure.step("Закрытие браузера"):
        browser.quit()

@pytest.mark.ui
@allure.title("Редирект на страницу авторизации при попытке оценить фильм")
@allure.story("Неавторизованный пользователь")
def test_film_rate(browser):
    film_rating = FilmRating(browser)
    with allure.step("Кликнуть на кнопку 'Оценить фильм'"):
        film_rating.click_rate()

    with allure.step("Кликнуть на оценку'9'"):    
        film_rating.film_rate()

    WebDriverWait(browser, 10).until(
        EC.url_contains("passport.yandex.ru")
    )

    with allure.step("Проверка редиректа на сайт для авторизации"): 
        assert "passport.yandex.ru" in browser.current_url

    with allure.step("Закрытие браузера"):
        browser.quit()

@allure.title("Редирект на страницу авторизации при попытке посмотреть фильмы")
@allure.story("Неавторизованный пользователь")
def test_kinopoisk_hd(browser):
    film_rating = KinopoiskHD(browser)
    with allure.step("Кликнуть на кнопку 'Онлайн-кинотеатр'"):
        film_rating.click_kinopoisk_hd()

    WebDriverWait(browser, 10).until(
        EC.url_contains("hd.kinopoisk.ru/")
    )

    with allure.step("Проверка редиректа на сайт для просмотра фильмов"): 
        assert "hd.kinopoisk.ru/" in browser.current_url
    with allure.step("Закрытие браузера"):
        browser.quit()

@pytest.mark.ui
@allure.title("Редирект на страницу авторизации при попытке добавить фильм в папку")
@allure.story("Неавторизованный пользователь")
def test_add_to_folder_without_login(browser):
    watch_film = AddToFolderFilm(browser)
    with allure.step("Кликнуть на кнопку 'Добавить в папку'"):
        watch_film.click_add()

    WebDriverWait(browser, 10).until(
        EC.url_contains("passport.yandex.ru")
    )

    with allure.step("Проверка редиректа на сайт для авторизации"): 
        assert "passport.yandex.ru" in browser.current_url

    with allure.step("Закрытие браузера"):
        browser.quit()

@pytest.mark.ui
@allure.title("Получение информации о режиссере")
@allure.story("Получение информации")
def test_director_info(browser):
    director_page = DirectorInfo(browser)
    expected_info = {
        'name_rus': 'Квентин Тарантино',
        'name_eng': 'Quentin Tarantino'
    }
    sleep(10)
    with allure.step('Получение информации о режиссере'):
        actual_info = director_page.get_director_info()
    with allure.step("Проверка всей информации о режиссере"):
        assert actual_info == expected_info
    with allure.step("Закрытие браузера"):
        browser.quit()