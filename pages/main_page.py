from appium.webdriver.common.appiumby import AppiumBy
from page_factory.button import Button
from page_factory.label import Label
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.trophy_button = Button(driver, (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[1]'
        ), "Trophy Button")

        self.fire_button = Button(driver, (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[2]'
        ), "Fire Button")

        self.profile_button = Button(driver, (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[3]'
        ), "Profile Button")

        self.profile_nav_button = Button(driver, (
            AppiumBy.XPATH,
            '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()]'
        ), "Profile Nav Button")

        self.tutors_nav_button = Button(driver, (
            AppiumBy.XPATH,
            '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-1]'
        ), "Tutors Nav Button")

        self.for_you_nav_button = Button(driver, (
            AppiumBy.XPATH,
            '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-2]'
        ), "For You Nav Button")

        self.my_plan_nav_button = Button(driver, (
            AppiumBy.XPATH,
            '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-3]'
        ), "My Plan Nav Button")

        self.current_level = Label(driver, (
            AppiumBy.XPATH,
            '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.TextView'
        ), "Current Level")

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
