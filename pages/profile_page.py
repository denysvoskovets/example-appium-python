from appium.webdriver.common.appiumby import AppiumBy
from page_factory.button import Button
from pages.base_page import BasePage

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.ukrainians_button = Button(
            driver,
            (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]'),
            "Ukrainians Button"
        )

    def tap_ukrainians_button(self):
        self.ukrainians_button.click()

