import allure
from Sprint_7.data import Urls
import requests


class TestGetOrderList:

    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что список заказов возвращается')
    def test_get_order_list_success(self):
        response = requests.get(Urls.ORDER)
        assert response.status_code == 200 and len(response.json()['orders']) > 0