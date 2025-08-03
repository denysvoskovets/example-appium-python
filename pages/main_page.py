from page_factory.button import Button
from page_factory.label import Label
from pages.base_page import BasePage


import pages.locators.main_page_locators as loc

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.trophy_button = Button(driver, self.get_locator(loc.TROPHY_BUTTON), "Trophy Button")
        self.fire_button = Button(driver, self.get_locator(loc.FIRE_BUTTON), "Fire Button")
        self.profile_button = Button(driver, self.get_locator(loc.PROFILE_BUTTON), "Profile Button")

        self.profile_nav_button = Button(driver, self.get_locator(loc.PROFILE_NAV_BUTTON), "Profile Nav Button")
        self.tutors_nav_button = Button(driver, self.get_locator(loc.TUTORS_NAV_BUTTON), "Tutors Nav Button")
        self.for_you_nav_button = Button(driver, self.get_locator(loc.FOR_YOU_NAV_BUTTON), "For You Nav Button")
        self.my_plan_nav_button = Button(driver, self.get_locator(loc.MY_PLAN_NAV_BUTTON), "My Plan Nav Button")

        self.current_level = Label(driver, self.get_locator(loc.CURRENT_LEVEL), "Current Level")


    def wait_until_loaded(self, timeout=None):
        self.profile_nav_button.should_be_visible(timeout)
        self.tutors_nav_button.should_be_visible(timeout)
        self.for_you_nav_button.should_be_visible(timeout)
        self.my_plan_nav_button.should_be_visible(timeout)

    def get_current_level(self) -> str:
        return self.current_level.get_text().strip()

    def scroll_up(self):
        self.scroll_vertically("up")

    def open_profile(self):
        self.profile_nav_button.click()
