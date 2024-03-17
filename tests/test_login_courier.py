import allure
from Sprint_7.data import Urls
from Sprint_7.helpers import Courier
import pytest
import requests


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что для зарегистрированного курьера доступна авторизация')
    def test_login_courier_success(self):
        payload = Courier.register_new_courier_and_return_login_password()
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        Courier.delete_courier(payload)
        assert response.status_code == 200 and len(str(response.json().get('id'))) > 0


    @allure.title('Авторизация курьера без обязательных полей')
    @allure.description('Проверка, что авторизация курьера без заполнения логина и пароля недоступна')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_missing_login(self, field):
        payload = Courier.register_new_courier_and_return_login_password()
        del payload[field]
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message') == 'Недостаточно данных для входа'


    @allure.title('Авторизация несуществующей учетной записи курьера')
    @allure.description('Проверка, что авторизация для несуществующей учетной записи курьера недоступна')
    def test_login_courier_account_not_exist(self):
        payload = Courier.generate_data_courier()
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and response.json().get('message') == 'Учетная запись не найдена'