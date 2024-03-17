import allure
import json
from Sprint_7.data import Urls
from Sprint_7.data import Order
import pytest
import requests


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('Проверка, что заказ успешно создается c разными цветами')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = Order.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Urls.ORDER, payload)
        assert response.status_code == 201 and len(str(response.json()['track'])) > 0