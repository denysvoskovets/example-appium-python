from appium.webdriver.common.appiumby import AppiumBy
from page_factory.button import Button
from page_factory.field import Field
from page_factory.label import Label
from page_factory.component import Component
from pages.base_page import BasePage
import time
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from utils.image_utils import ImageUtils


class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.image_utils = ImageUtils(driver)
        self.driver = driver

        self.get_started_button = Button(driver, (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").childSelector(new UiSelector().text("GET STARTED"))'), "Get Started")
        self.i_have_an_account_button = Button(driver, (AppiumBy.XPATH, '//android.view.View[./android.widget.TextView[@text="I HAVE AN ACCOUNT"]]'), "I Have An Account")

        self.log_in_text = Label(driver, (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")'), "Login Label")
        self.sign_up_text = Label(driver, (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")'), "Signup Label")
        self.sign_up_nav_button = Button(driver, (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")'), "Signup Nav Button")

        self.email_field = Field(driver, (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]'), "Email Field")
        self.password_field = Field(driver, (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]'), "Password Field")
        self.password_eye_button = Button(driver, (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]/android.view.View'), "Password Eye")

        self.login_button = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="LOG IN"]'), "Login Button")
        self.sign_up_button = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="SIGN UP"]'), "Signup Button")

        self.oops_label = Label(driver, (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]/following-sibling::android.widget.TextView[1]'), "Oops Label")
        self.wrong_password_label = Label(driver, (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]/following-sibling::android.widget.TextView'), "Wrong Password Label")

        self.setting_account_label = Label(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="Setting up your learning experience"]'), "Setting Account Label")

        self.english_selector = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="English"]'), "English Selector")
        self.instructions_label = Label(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="Instructions should be in:"]'), "Instructions Label")
        self.continue_button = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]'), "Continue Button")
        self.beginner_button = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="Beginner"]'), "Beginner Button")

        self.motivation_elements = Component(driver, (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View'), "Motivation Items")
        self.motivation_continue_button = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]'), "Motivation Continue Button")
        self.topic_yes_button = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="YES"]/preceding-sibling::android.view.View[2]'), "Yes Topic Button")
        self.grammar_skill = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="Grammar"]'), "Grammar Skill")
        self.five_mins_element = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="5 min"]'), "5 Min")
        self.enjoy_label = Label(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="Enjoyed by 10M people"]'), "Enjoy Label")
        self.sign_up_with_email = Button(driver, (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up with email"]'), "Sign Up With Email")

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
