from page_factory.button import Button
from pages.base_page import BasePage
import pages.locators.profile_page_locators as loc


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.ukrainians_button = Button(driver, self.get_locator(loc.UKRAINIANS_BUTTON), "Ukrainians Button")

    def tap_ukrainians_button(self):
        self.ukrainians_button.click()

