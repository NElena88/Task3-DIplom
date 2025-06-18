import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_until_not_visible(OrderFeedLocators.OVERLAY)

    @allure.step('Кликаем на кнопку Лента Заказов')
    def click_button_order_feed(self):
        self.click_on_element(OrderFeedLocators.ORDER_FEED_BTN)

    @allure.step('Ожидаем появления кнопки Лента заказов')
    def wait_button_order_feed(self):
        self.wait_for_element(OrderFeedLocators.ORDER_FEED_BTN)

    @allure.step('Получаем текст кнопки Лента Заказов')
    def get_text_button_order_feed(self):
        return self.get_text_on_element(OrderFeedLocators.ORDER_FEED_BTN)

    @allure.step('Получаем текст заголовка Лента заказов')
    def get_text_header_order_feed(self):
        return self.get_text_on_element(OrderFeedLocators.ORDER_FEED_HEADER)

    @allure.step('Ожидаем появления заголовка Лента заказов')
    def wait_header_order_feed(self):
        self.wait_for_element(OrderFeedLocators.ORDER_FEED_HEADER)

    @allure.step('Ожидаем появления всплывающего окна с заголовком Идентификатор заказа')
    def wait_header_id_order(self):
        self.wait_for_element(OrderFeedLocators.HEADER_ID_ORDER)

    @allure.step('Дождаться прогрузки анимации и формирования номера заказа')
    def wait_for_loading_animation_end(self):
        self.wait_until_not_visible(OrderFeedLocators.LOADING_ANIMATION)

    @allure.step('Получаем номер заказа на всплывающем окне')
    def get_order_number(self):
        self.wait_for_loading_animation_end()
        return self.get_text_on_element(OrderFeedLocators.ORDER_ID)

    @allure.step('Ожидаем появления кнопки Конструктор')
    def wait_button_constructor(self):
        self.wait_for_element(OrderFeedLocators.BTN_CONSTRUCTOR)

    @allure.step('Скролл до элемента Х на всплывающем окне')
    def scroll_to_x_on_popup_and_close(self):
        self.scroll_to_element(OrderFeedLocators.CLOSE_POPUP_ID_ORDER)
        close_btn = self.driver.find_element(*OrderFeedLocators.CLOSE_POPUP_ID_ORDER)
        close_btn.click()

    @allure.step('Ожидаем Х для закрытия всплывающего окна')
    def wait_x_on_popup(self):
        self.wait_for_element(OrderFeedLocators.CLOSE_POPUP_ID_ORDER)

    @allure.step('Закрываем окно с номером id заказа с помощью X')
    def click_on_close_popup_with_id_order(self):
        self.click_on_element(OrderFeedLocators.CLOSE_POPUP_ID_ORDER)

    @allure.step("Получаем значение счётчика всех заказов на странице 'Лента заказов'")
    def get_orders_counter(self, locator):
        number = self.get_text_on_element(locator)
        return int(number)

    @allure.step("Получение списка номеров заказов в ленте заказов")
    def get_all_order_numbers_feed(self):  # получить весь список заказов в ленте
        self.wait_for_element(OrderFeedLocators.ORDER_NUMBERS_IN_PROGRESS)
        elements = self.driver.find_elements(*OrderFeedLocators.ORDER_NUMBERS_IN_PROGRESS)
        cleaned_numbers = []
        for el in elements:
            text = el.text.strip()
            if text.startswith("#"):
                text = text[1:]  # Удаляем "#"
            if text:
                cleaned_numbers.append(text.lstrip('0'))  # удаляем ведущие нули

        return cleaned_numbers




