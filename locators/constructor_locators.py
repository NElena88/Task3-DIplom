from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BTN_CONSTRUCTOR = (By.XPATH, '//a[p[text()="Конструктор"]]')
    HEADER_MAKE_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')
    BTN_ORDER_TAPE = (By.XPATH, '//p[text()="Лента Заказов"]')
    HEADER_ORDER_TAPE = (By.XPATH, '//h1[text()="Лента заказов"]')
    INGR_BUN = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @draggable='true']//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH')]")
    COUNTER_INGR_BUN = (By.XPATH, "//div[contains(@class, 'counter_counter')]/p[contains(@class, 'counter_counter__num')]")
    CONSTRUCTOR = (By.XPATH, '//li[.//span[contains(text(), "Перетяните булочку сюда")]]')
    POPUP_HEADER_INGR = (By.XPATH,'//h2[text()="Детали ингредиента"]')
    POPUP_CLOSE = (By.XPATH, '//button[contains(@class, "modal__close")]')
    INGR_SAUCE = (By.XPATH, "//a[@draggable='true' and .//p[text()='Соус Spicy-X']]")
    INGR_SAUCE_IN_CONST = (By.XPATH, "//span[@class='constructor-element__text' and text()='Соус Spicy-X']")
    BTN_LOGIN_ACCOUNT = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    COUNTER_INGR_SAUCE = (By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa72")]//p[contains(@class, "counter_counter__num__3nue1")]')
    CREATE_ORDER = (By.XPATH, '//div[contains(@class, "BurgerConstructor_basket__container")]//button[text()="Оформить заказ"]')
    HEADER_ID_ORDER = (By.XPATH, '//p[text()="идентификатор заказа"]')
    POPUP_ID_ORDER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(@class, "text_type_digits-large")]')
    CLOSE_POPUP_ID_ORDER = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

