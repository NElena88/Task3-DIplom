import time

import allure
from data import *
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage


class TestCoreFunctionality:
    @allure.title('Переход по клику на "Конструктор"')
    def test_open_constructor(self, driver):
        constructor_page = ConstructorPage(driver)
        auth_page = AuthPage(driver)
        constructor_page.main_page_loading_wait() # ждем исчезновения оверлея
        constructor_page.click_button_sign_in() # надимаем на кнопку Войти в аккаунт
        auth_page.wait_visibility_header_entrance() # ждем появления заголовка Вход
        constructor_page.click_button_constructor() # нажимаем на кнопку Конструктор
        assert constructor_page.get_make_burger_text() == Text.MAKE_BURGER_TXT # проверяем, что отобразился заголовок Соберите бургер

    @allure.title('Переход по клику на "Лента Заказов"')
    def test_open_list_orders(self, driver):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        constructor_page.main_page_loading_wait() # ждем исчезновения оверлея
        order_feed_page.click_button_order_feed() # нажимаем на кнопку Лента Заказов
        assert order_feed_page.get_text_header_order_feed() == Text.ORDER_FEED_TXT # проверяем, что отобразился заголовок Лента Заказов

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_popup_details_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.main_page_loading_wait() # ждем исчезновения оверлея
        constructor_page.click_on_ingredient_bun() # нажимаем на ингредиент булка
        constructor_page.wait_for_header_popup() # ждем появления заголовка на всплываюшем окне
        assert constructor_page.get_details_ingredient_text() == Text.DETAIL_INGREDIENT # проверяем, что текст заголовка Детали ингредиента

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_popup_details_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.main_page_loading_wait() # ждем исчезновения оверлея
        constructor_page.click_on_ingredient_bun() # нажимаем на ингредиент булка
        constructor_page.wait_for_header_popup() # ждем появления заголовка на всплываюшем окне
        constructor_page.close_popup_with_ingredient_details() # закрываем всплываюшее окно по крестику
        assert constructor_page.get_make_burger_text() == Text.MAKE_BURGER_TXT # проверяем, что отобразился заголовок Соберите бургер

    @allure.title('При добавлении ингредиента в заказ, увеличивается счетчик данного ингредиента')
    def test_increase_the_ingredient_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.main_page_loading_wait() # ждем исчезновения оверлея
        count_ingredient_before = constructor_page.get_count_ingredient_sauce() # проверяем количество ингредиента до добавления в конструктор/корзину
        constructor_page.drag_sauce_to_constructor() # перетаскиваем соус в конструктор
        count_ingredient_after = constructor_page.get_count_ingredient_sauce() # проверяем количество ингредиента после добавления в конструктор
        assert count_ingredient_after == count_ingredient_before + 1 # проверяем, что счетчик увеличился на 1
