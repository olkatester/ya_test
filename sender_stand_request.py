import configuration
import requests
import data


def post_new_order(body):    #post-запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=body)

response_new_order = post_new_order(data.order_body)


track_number = str(response_new_order.json()["track"])  # сохранили в переменную track_number номер трека созданного заказа, перевели число в строку


def get_order_track(): # выполнили запрос на получение заказа по треку заказа
    return requests.get(configuration.URL_SERVICE+configuration.NEW_TRACK+"?t="+track_number)


response_order_track_status = get_order_track().status_code #код ответа по запросу заказа по треку
