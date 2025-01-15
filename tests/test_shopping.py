import random
import allure
import pytest
from pages.buy_page import BuyPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from config.data import Data

@allure.feature("Shopping Cart and Checkout")
@allure.severity(allure.severity_level.BLOCKER)
class TestShopping:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.buy_page = BuyPage(self.driver)

    @allure.title("Вход в аккаунт")
    #@pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_submit()

    @allure.title("Добавление товара в корзину")
    #@pytest.mark.smoke
    def test_add(self):
        self.dashboard_page.is_opened()
        self.dashboard_page.add_product()
        self.dashboard_page.is_add_product()
        self.dashboard_page.open_cart()

    @allure.title("Покупка товара")
    #@pytest.mark.smoke
    def test_buy(self):
        self.buy_page.is_opened()
        self.buy_page.save_target_price()

        self.buy_page.open_form()
        self.buy_page.is_opened_buy_form()
        self.buy_page.fill_out_first_name(f'tester_{random.randint(1, 100)}')
        self.buy_page.fill_out_last_name('last_name')
        self.buy_page.fill_out_code(random.randint(100, 900))
        self.buy_page.continue_form()

        self.buy_page.is_opened_buy_finish()
        self.buy_page.check_price()

        self.buy_page.accept()
        self.buy_page.is_opened_buy_complete()
        self.buy_page.check_buy()
        self.buy_page.make_screenshot("Success")