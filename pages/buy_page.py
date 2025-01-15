import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links

class BuyPage(BasePage):

    PAGE_URL = Links.BUY_PAGE
    BUY_FORM_PAGE = Links.BUY_FORM_PAGE
    BUY_COMPLETE_PAGE = Links.BUY_COMPLETE_PAGE
    BUY_FINISH_PAGE = Links.BUY_FINISH_PAGE

    """Проверка цены"""
    PRICE_FIELD = ("xpath", "//div[@class='inventory_item_price']")
    TAX_FIELD = ("xpath", "//div[@class='summary_tax_label']")
    TOTAL_FIELD = ("xpath", "//div[@class='summary_total_label']")
    """Заполнение формы"""
    CHECKOUT_FIELD = ("xpath", "//button[@name='checkout']")
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    CODE_FIELD = ("xpath", "//input[@name='postalCode']")
    CONTINUE_FIELD = ("xpath", "//input[@name='continue']")
    """Оплата"""
    FINISH_FIELD = ("xpath", "//button[@name='finish']")
    CHECK_FINISH_FIELD = ("xpath", "//h2[@class='complete-header']")


    @allure.step("Запомнил стоимость товара в корзине")
    def save_target_price(self):
        self.target = float(self.driver.find_element(*self.PRICE_FIELD).text[1:])

    """Заполнение Формы"""

    @allure.step("Click 'Checkout'")
    def open_form(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_FIELD)).click()
    def is_opened_buy_form(self):
        with allure.step("Is opened buy_form_page"):
            self.wait.until(EC.url_to_be(self.BUY_FORM_PAGE))


    def fill_out_first_name(self, first_name):
        with allure.step(f"Ввод в поле 'first name' - '{first_name}'"):
            self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(first_name)

    def fill_out_last_name(self, last_name):
        with allure.step(f"Ввод в поле 'last name' - '{last_name}'"):
            self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(last_name)

    def fill_out_code(self, code):
        with allure.step(f"Ввод в поле 'zip code' - '{code}'"):
            self.wait.until(EC.element_to_be_clickable(self.CODE_FIELD)).send_keys(code)

    @allure.step("Click 'Continue'")
    def continue_form(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_FIELD)).click()
    def is_opened_buy_finish(self):
        with allure.step("Is opened buy_finish_page"):
            self.wait.until(EC.url_to_be(self.BUY_FINISH_PAGE))

    """Сравнение цены"""

    @allure.step('Сравнение цены товара с вычетом налога и общей стоимостью')
    def check_price(self):
        tax = float(self.driver.find_element(*self.TAX_FIELD).text.split().pop(1)[1:])
        total = float(self.driver.find_element(*self.TOTAL_FIELD).text.split().pop(1)[1:])
        assert total*100 - tax*100 == self.target*100, 'Цена товара другая'

    @allure.step("Click 'Finish'")
    def accept(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_FIELD)).click()
    def is_opened_buy_complete(self):
        with allure.step("Is opened buy_complete_page"):
            self.wait.until(EC.url_to_be(self.BUY_COMPLETE_PAGE))

    @allure.step("Проверка успешного офрмления заказа")
    def check_buy(self):
        self.check_phrase = self.driver.find_element(*self.CHECK_FINISH_FIELD).text
        assert 'Thank' in self.check_phrase, 'Оплата не прошла'
