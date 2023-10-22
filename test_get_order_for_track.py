# Ольга Каплина, 9-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_positive_assert(): # статус кода 200 (позитивная проверка)
    assert sender_stand_request.response_order_track_status == 200

def test_negative_assert_no_data(): # статус кода 400 (негативная проверка, нет данных для поиска)
    assert sender_stand_request.response_order_track_status ==400

def test_negative_assert_no_order(): # статус кода 400 (негативная проверка, заказ не найден)
    assert sender_stand_request.response_order_track_status ==404
