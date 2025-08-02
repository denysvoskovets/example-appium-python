import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.trophy_button = (AppiumBy.XPATH,
                              '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[1]')
        self.fire_button = (AppiumBy.XPATH,
                            '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[2]')
        self.profile_button = (AppiumBy.XPATH,
                               '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[3]')

        self.profile_nav_button = (AppiumBy.XPATH,
                                   '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()]')
        self.tutors_nav_button = (AppiumBy.XPATH,
                                  '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-1]')
        self.for_you_nav_button = (AppiumBy.XPATH,
                                   '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-2]')
        self.my_plan_nav_button = (AppiumBy.XPATH,
                                   '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-3]')

        self.current_level = (AppiumBy.XPATH,
                              '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.TextView')

    @allure.step("Check MainPage loaded")
    def wait_until_loaded(self, timeout=15):
        self.wait_for_element(*self.profile_nav_button, condition=EC.visibility_of_element_located, timeout=timeout)
        self.wait_for_element(*self.tutors_nav_button, condition=EC.visibility_of_element_located, timeout=timeout)
        self.wait_for_element(*self.for_you_nav_button, condition=EC.visibility_of_element_located, timeout=timeout)
        self.wait_for_element(*self.my_plan_nav_button, condition=EC.visibility_of_element_located, timeout=timeout)

    @allure.step("Check current level")
    def get_current_level(self):
        return self.wait_for_element(*self.current_level, condition=EC.visibility_of_element_located)

    def scroll_up(self):
        self.scroll_vertically('up')

    @allure.step("Open profile")
    def open_profile(self):
        self.click(*self.profile_nav_button)
