import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from pages.base_page import BasePage
from utils.image_utils import ImageUtils


class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.image_utils = ImageUtils(driver)

        self.get_started_button = (AppiumBy.ANDROID_UIAUTOMATOR,
                                   'new UiSelector().className("android.view.View").childSelector(new UiSelector().text("GET STARTED"))')
        self.i_have_an_account_button = (AppiumBy.XPATH,
                                         '//android.view.View[./android.widget.TextView[@text="I HAVE AN ACCOUNT"]]')

        self.log_in_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")')
        self.sign_up_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")')
        self.sign_up_nav_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")')
        self.email_field = (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]')
        self.password_field = (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]')
        self.password_eye_button = (AppiumBy.XPATH,
                                    '//android.widget.ScrollView/android.widget.EditText[2]/android.view.View')

        self.login_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOG IN"]')
        self.sign_up_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="SIGN UP"]')

        self.oops_label = (AppiumBy.XPATH,
                           '//android.widget.ScrollView/android.widget.EditText[1]/following-sibling::android.widget.TextView[1]')
        self.wrong_password_label = (AppiumBy.XPATH,
                                     '//android.widget.ScrollView/android.widget.EditText[2]/following-sibling::android.widget.TextView')

        self.setting_account_label = (AppiumBy.XPATH,
                                      '//android.widget.TextView[@text="Setting up your learning experience"]')

        self.english_selector = (AppiumBy.XPATH, '//android.widget.TextView[@text="English"]')
        self.instructions_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Instructions should be in:"]')
        self.continue_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]')
        self.beginner_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="Beginner"]')
        self.motivation_elements = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View')
        self.motivation_continue_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]')
        self.topic_yes_button = (AppiumBy.XPATH,
                                 '//android.widget.TextView[@text="YES"]/preceding-sibling::android.view.View[2]')
        self.grammar_skill = (AppiumBy.XPATH, '//android.widget.TextView[@text="Grammar"]')
        self.five_mins_element = (AppiumBy.XPATH, '//android.widget.TextView[@text="5 min"]')
        self.enjoy_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enjoyed by 10M people"]')
        self.sign_up_with_email = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up with email"]')

    @allure.step("Tap get started")
    def tap_get_started(self):
        self.click(*self.get_started_button)

    @allure.step("Tap I_have_an_account")
    def tap_i_have_an_account(self):
        self.click(*self.i_have_an_account_button)

    def wait_for_login_text(self):
        return self.wait_for_element(*self.log_in_text)

    @allure.step("Fill email field")
    def fill_email(self, email: str):
        email_input = self.wait_for_element(*self.email_field)
        email_input.send_keys(email)

    @allure.step("Fill password field")
    def fill_password(self, password: str):
        password_input = self.wait_for_element(*self.password_field)
        password_input.send_keys(password)

    @allure.step("Tap login button")
    def tap_login_button(self):
        self.click(*self.login_button)

    @allure.step("Tap to SignUp menu")
    def tap_navigate_signup_menu(self):
        self.click(*self.sign_up_nav_button)

    @allure.step("Tap SignUp button")
    def tap_signup_button(self):
        self.click(*self.sign_up_button)

    def get_email_error_label(self):
        return self.wait_for_element(*self.oops_label, condition=EC.element_to_be_clickable)

    def get_password_error_label(self):
        return self.wait_for_element(*self.wrong_password_label, condition=EC.element_to_be_clickable)

    @allure.step("Tap on Eye")
    def tap_on_eye(self):
        self.click(*self.password_eye_button)

    def get_password_text(self):
        return self.wait_for_element(*self.password_field, condition=EC.element_to_be_clickable).text

    @allure.step("Select English")
    def tap_english_selector(self):
        self.click(*self.english_selector)

    def wait_instructions(self):
        return self.wait_for_element(*self.instructions_label)

    @allure.step("Tap Continue")
    def tap_continue(self):
        self.click(*self.continue_button)

    @allure.step("Select beginner")
    def tap_beginner(self):
        self.click(*self.beginner_button)

    @allure.step("Select motivations on indexes {indexes}")
    def select_and_compare_motivations(self, count=1, indexes=None, check_visual=False):
        elements = self.wait_for_all_elements(*self.motivation_elements)

        if indexes is None:
            indexes = list(range(min(count, len(elements))))

        for i in indexes:
            el = elements[i]

            before = self.image_utils.take_screenshot_as_image()
            el.click()
            time.sleep(1)

            after = self.image_utils.take_screenshot_as_image()

            if check_visual:
                are_similar, diff = self.image_utils.compare_images(before, after)

                before.save(f"utils/screenshots/motivation_{i}_before.png")
                after.save(f"utils/screenshots/motivation_{i}_after.png")
                diff.save(f"utils/screenshots/motivation_{i}_diff.png")

                assert not are_similar, f"Motivation {i} did not visually change after selection"

    @allure.step("Tap Continue")
    def tap_motivations_continue(self):
        self.click(*self.motivation_continue_button)

    @allure.step("Tap Yes topic")
    def tap_topic_yes(self):
        self.click(*self.topic_yes_button)

    def tap_topic_yes_until_gone(self, count=12, delay_seconds=.7):
        wait = WebDriverWait(self.driver, delay_seconds)
        for i in range(count):
            try:
                button = wait.until(EC.element_to_be_clickable(self.topic_yes_button))
                button.click()
            except (TimeoutException, StaleElementReferenceException):
                break
            time.sleep(delay_seconds)

    @allure.step("Select skill")
    def tap_skill(self):
        self.click(*self.grammar_skill)

    @allure.step("Select mins")
    def tap_mins(self):
        self.click(*self.five_mins_element)

    @allure.step("Tap enjoy")
    def tap_enjoy(self):
        self.wait_for_element(*self.enjoy_label, condition=EC.element_to_be_clickable)
        self.tap_continue()

    def wait_for_sign_up_button(self):
        return self.wait_for_element(*self.sign_up_with_email)

    def perform_login(self, email: str, password: str):
        self.tap_i_have_an_account()
        self.wait_for_login_text()
        self.fill_email(email)
        self.fill_password(password)
        self.tap_login_button()
