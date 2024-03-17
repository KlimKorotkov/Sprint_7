Sprint_7 Автотесты API сервиса Яндекс Самокат

Tests:
test_create_courier
test_create_order
test_get_order_list
test_login_courier

Запуск тестов: pytest -v ./tests
Генерация отчета Allure: pytest -v ./tests --alluredir=allure_results
Формирование отчета Allure: allure serve allure_results