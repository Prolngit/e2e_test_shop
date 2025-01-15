from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

import allure
from allure_commons.types import AttachmentType

class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Open page')
    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"{self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screen_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screen_name,
            attachment_type=AttachmentType.PNG
        )