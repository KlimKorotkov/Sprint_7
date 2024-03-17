class Urls:
    CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    LOGIN_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class Order:
    order_data = {
        "firstName": "Rick",
        "lastName": "Sanchez",
        "address": "Earth, 543",
        "metroStation": 1,
        "phone": "+7 900 999 66 66",
        "rentTime": 8,
        "deliveryDate": "2056-09-09",
        "comment": "Morty, let's go",
        "color": []
    }