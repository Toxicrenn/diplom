import allure
from service.api_kinopoisk import KinopoiskApi

API_KEY = "f352483e-2634-403e-a05d-cb6e71b3998e"
OLD_KEY = "12345678-90ab-cdef-1234-567890abcdef"
api = KinopoiskApi(API_KEY)
api_with_old_token = KinopoiskApi(OLD_KEY)

@allure.title("Успешное получение данных о фильме по ID")
@allure.story("Получение информации о фильме")
def test_get_info_by_id():
    with allure.step("Получить информацию о фильме через API по ID"):
        resp = api.get_info_by_id()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200

@allure.title("Успешное получение данных о наградах фильма по ID")
@allure.story("Получение информации о фильме")
def test_get_info_about_prizes():
    with allure.step("Получить информацию о наградах фильма через API по ID"):
        resp = api.get_info_about_prizes()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200

@allure.title("Успешное получение данных о прокате фильма по ID")
@allure.story("Получение информации о фильме")
def test_get_info_about_rental():
    with allure.step("Получить информацию о прокате фильма через API по ID"):
        resp = api.get_info_about_rental()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200

@allure.title("Ошибка при запросе получения информации о фильме без id")
@allure.story("Получение информации о фильме")
def test_get_info_without_id():
    with allure.step("Получить информацию о фильме через API без ID"):
        resp = api.get_info_without_id()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 400

@allure.title("Ошибка при запросе получения информации о фильме без токена")
@allure.story("Получение информации о фильме")
def test_get_info_without_token():
    with allure.step("Получить информацию о фильме через API без токена"):
        resp = api.get_info_without_token()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 401

@allure.title("Ошибка при запросе получения информации о фильме со старым токеном")
@allure.story("Получение информации о фильме")
def test_get_info_with_old_token():
    with allure.step("Получить информацию о фильме через API со старым токеном"):
        resp = api_with_old_token.get_info_by_id()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 401

@allure.title("Ошибка при запросе получения информации о фильме с неправильным id")
@allure.story("Получение информации о фильме")
def test_get_info_with_wrong_id():
    with allure.step("Получить информацию о фильме через API с неправильным id"):
        resp = api.get_info_with_wrong_id()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 404

@allure.title("Ошибка при запросе получения информации о фильме при использовании неверного метода api")
@allure.story("Получение информации о фильме")
def test_get_info_with_wrong_api_method():
    with allure.step("Получить информацию о фильме через API с неправильным методом api"):
        resp = api.get_info_with_wrong_api_method()
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 500