import time
import allure
import pytest
from locators.order_feed_locators import OrderFeedLocators


class TestOrderFeed:

    @allure.title('При создании нового заказа счетчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.COUNTER_ORDERS_ALL,
                                         OrderFeedLocators.COUNTER_ORDERS_TODAY])
    def test_orders_increase_count_with_new_order(self, driver, login, constructor_page, order_feed_page, counter):
        constructor_page.main_page_loading_wait()  # ожидаем исчезновения оверлея
        order_feed_page.click_button_order_feed()  # переходим в раздел Лента Заказов
        order_feed_page.wait_header_order_feed() # ожидаем появления заголовка Лента заказов
        count_orders = order_feed_page.get_orders_counter(counter)  # получаем текущее значение счетчика дл создания заказа
        order_feed_page.wait_button_constructor() # ожидаем появления кнопки Конструктор
        constructor_page.click_button_constructor()  # переходим в конструктор
        constructor_page.wait_for_header_make_burger()  # ожидаем заголовок Соберите бургер
        constructor_page.create_order() # создаем заказ
        order_feed_page.wait_header_id_order()  # ждем появления всплывающего окна с номером заказа
        order_feed_page.wait_for_loading_animation_end() # ждем загрузки анимации
        order_feed_page.click_on_close_popup_with_id_order()  # закрываем всплывающее окно с номером заказа
        order_feed_page.wait_button_order_feed() # ожидаем появления кнопки Лента заказов
        order_feed_page.click_button_order_feed()  # повторно переходим в Ленту Заказов
        count_orders_new = order_feed_page.get_orders_counter(counter)  # получаем новое значение счетчика после создания заказа
        assert count_orders_new > count_orders  # проверяем, что значение счетчика увеличилось

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_in_progress_section(self, driver, login, constructor_page, order_feed_page):
        constructor_page.main_page_loading_wait()  # ожидаем исчезновения оверлея
        constructor_page.wait_for_header_make_burger() # ожидаем заголовок Соберите бургер
        constructor_page.create_order() # создаем заказ
        order_feed_page.wait_header_id_order() # ожидаем заголовок всплывающего окна с номером заказа
        order_number = order_feed_page.get_order_number() # получаем номер заказа в окне
        order_feed_page.wait_for_loading_animation_end()  # ждем загрузки анимации
        order_feed_page.scroll_to_x_on_popup_and_close() # закрываем всплывающее окно с номером id заказа
        order_feed_page.wait_button_order_feed() # ожидаем появления кнопки Лента заказов
        order_feed_page.click_button_order_feed() # переходим в раздел Лента Заказов
        order_feed_page.wait_header_order_feed() # ожидаем появления заголовка Лента заказов
        actual_number = order_feed_page.get_all_order_numbers_feed() # получаем список всех номеров в разделе В работе
        assert order_number in actual_number # сравниваем результат
