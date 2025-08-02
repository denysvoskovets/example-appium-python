from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.ukrainians_button = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]')

    def get_ukrainians_button(self):
        return self.wait_for_element(*self.ukrainians_button)
