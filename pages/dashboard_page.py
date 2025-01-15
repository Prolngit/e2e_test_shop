import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    PRODUCT_FIELD = ("xpath", "//button[contains(@name, 'backpack')]")
    CART_FIELD = ("xpath", "//a[@class='shopping_cart_link']")
    CART_INDEX_FIELD = ("xpath", "//a[@class='shopping_cart_link']/span")


    @allure.step("Добавить товар в корзину")
    def add_product(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_FIELD)).click()

    @allure.step("Проверка на визуализацию товара в корзине")
    def is_add_product(self):
        assert self.driver.find_element(*self.CART_INDEX_FIELD).text == '1', 'Товар не добавлен'

    @allure.step("Открыть корзину")
    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_FIELD)).click()