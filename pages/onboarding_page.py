from page_factory.button import Button
from page_factory.field import Field
from page_factory.label import Label
from page_factory.component import Component
from pages.base_page import BasePage
import time
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from utils.image_utils import ImageUtils
import pages.locators.onboarding_page_locators as loc


class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.image_utils = ImageUtils(driver)

        self.get_started_button = Button(driver, self.get_locator(loc.GET_STARTED_BUTTON), "Get Started")
        self.i_have_an_account_button = Button(driver, self.get_locator(loc.I_HAVE_AN_ACCOUNT_BUTTON),
                                               "I Have An Account")

        self.log_in_text = Label(driver, self.get_locator(loc.LOG_IN_TEXT), "Login Label")
        self.sign_up_text = Label(driver, self.get_locator(loc.SIGN_UP_TEXT), "Signup Label")
        self.sign_up_nav_button = Button(driver, self.get_locator(loc.SIGN_UP_NAV_BUTTON), "Signup Nav Button")

        self.email_field = Field(driver, self.get_locator(loc.EMAIL_FIELD), "Email Field")
        self.password_field = Field(driver, self.get_locator(loc.PASSWORD_FIELD), "Password Field")
        self.password_eye_button = Button(driver, self.get_locator(loc.PASSWORD_EYE_BUTTON), "Password Eye")

        self.login_button = Button(driver, self.get_locator(loc.LOGIN_BUTTON), "Login Button")
        self.sign_up_button = Button(driver, self.get_locator(loc.SIGN_UP_BUTTON), "Signup Button")

        self.oops_label = Label(driver, self.get_locator(loc.OOPS_LABEL), "Oops Label")
        self.wrong_password_label = Label(driver, self.get_locator(loc.WRONG_PASSWORD_LABEL), "Wrong Password Label")

        self.setting_account_label = Label(driver, self.get_locator(loc.SETTING_ACCOUNT_LABEL), "Setting Account Label")

        self.english_selector = Button(driver, self.get_locator(loc.ENGLISH_SELECTOR), "English Selector")
        self.instructions_label = Label(driver, self.get_locator(loc.INSTRUCTIONS_LABEL), "Instructions Label")
        self.continue_button = Button(driver, self.get_locator(loc.CONTINUE_BUTTON), "Continue Button")
        self.beginner_button = Button(driver, self.get_locator(loc.BEGINNER_BUTTON), "Beginner Button")

        self.motivation_elements = Component(driver, self.get_locator(loc.MOTIVATION_ELEMENTS), "Motivation Items")
        self.motivation_continue_button = Button(driver, self.get_locator(loc.MOTIVATION_CONTINUE_BUTTON),
                                                 "Motivation Continue Button")
        self.topic_yes_button = Button(driver, self.get_locator(loc.TOPIC_YES_BUTTON), "Yes Topic Button")
        self.grammar_skill = Button(driver, self.get_locator(loc.GRAMMAR_SKILL), "Grammar Skill")
        self.five_mins_element = Button(driver, self.get_locator(loc.FIVE_MINS_ELEMENT), "5 Min")
        self.enjoy_label = Label(driver, self.get_locator(loc.ENJOY_LABEL), "Enjoy Label")
        self.sign_up_with_email = Button(driver, self.get_locator(loc.SIGN_UP_WITH_EMAIL), "Sign Up With Email")

    def start_onboarding(self):
        self.get_started_button.click()

    def tap_i_have_an_account(self):
        self.i_have_an_account_button.click()

    def fill_email(self, email: str):
        self.email_field.fill(email)

    def fill_password(self, password: str):
        self.password_field.fill(password)

    def tap_login_button(self):
        self.login_button.click()

    def tap_navigate_signup_menu(self):
        self.sign_up_nav_button.click()

    def tap_signup_button(self):
        self.sign_up_button.click()

    def tap_on_eye(self):
        self.password_eye_button.click()

    def tap_english_selector(self):
        self.english_selector.click()

    def tap_continue(self):
        self.continue_button.click()

    def tap_beginner(self):
        self.beginner_button.click()

    def select_and_compare_motivations(self, count=1, indexes=None, check_visual=False):
        elements = self.motivation_elements.get_elements()

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

    def tap_motivations_continue(self):
        self.motivation_continue_button.click()

    def tap_topic_yes(self):
        self.topic_yes_button.click()

    def tap_topic_yes_until_gone(self, count=12, delay_seconds=0.7):
        wait = WebDriverWait(self.driver, delay_seconds)
        for i in range(count):
            try:
                self.topic_yes_button.is_displayed()
                self.topic_yes_button.click()
            except (TimeoutException, StaleElementReferenceException):
                break
            time.sleep(delay_seconds)

    def tap_skill(self):
        self.grammar_skill.click()

    def tap_mins(self):
        self.five_mins_element.click()

    def tap_enjoy(self):
        self.enjoy_label.is_displayed()
        self.tap_continue()

    def wait_for_sign_up_button(self):
        self.sign_up_with_email.is_displayed()

    def perform_login(self, email: str, password: str):
        self.tap_i_have_an_account()
        self.log_in_text.is_displayed()
        self.fill_email(email)
        self.fill_password(password)
        self.tap_login_button()
