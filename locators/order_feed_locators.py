from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_POP_UP = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    CLOSE_POPUP_ID_ORDER = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    ORDER_FEED_BTN = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_FEED_HEADER = (By.XPATH, '//h1[contains(@class, "text_type_main-large") and text()="Лента заказов"]')
    BTN_CONSTRUCTOR = (By.XPATH, '//a[p[text()="Конструктор"]]')
    COUNTER_ORDERS_ALL = (By.XPATH, "(.//p[contains(@class, 'OrderFeed_number__2MbrQ text text_type_digits-large')])[1]")
    COUNTER_ORDERS_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]")
    ORDER_ID = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    LOADING_ANIMATION = (By.XPATH, './/img[@src="./static/media/loading.89540200.svg"]')

    ORDER_FEED = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]')
    HEADER_IN_WORK = (By.XPATH, '//p[text()="В работе:"]')
    ORDER_NUMBERS_IN_PROGRESS = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderReadyContainer')]//ul/li/p[contains(@class, 'text_type_digits-default')]")

    FIRST_ORDER_IN_WORKING_LIST = (By.XPATH, './/li[@class="text text_type_digits-default mb-2"]')
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    HEADER_ID_ORDER = (By.XPATH, '//p[text()="идентификатор заказа"]')
    POPUP_ID_ORDER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(@class, "text_type_digits-large")]')