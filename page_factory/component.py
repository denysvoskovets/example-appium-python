import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class Component:
    def __init__(self, driver, locator: tuple, name: str = None, timeout: int = 10):
        self.driver = driver
        self.locator = locator
        self.name = name or locator[1]
        self.timeout = timeout

    @property
    def type_of(self) -> str:
        return "component"

    def wait_for_element(self, condition=EC.presence_of_element_located, timeout=None):
        by, value = self.locator
        logger.info(f"Waiting for element by {by}='{value}' with timeout {(timeout or self.timeout)}s")
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            condition((by, value))
        )

    def get_element(self):
        with allure.step(f'Getting {self.type_of} "{self.name}" with locator {self.locator}'):
            return self.wait_for_element()

    def get_elements(self):
        with allure.step(f'Getting all {self.type_of}s "{self.name}" with locator {self.locator}'):
            by, value = self.locator
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )

    def click(self):
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):
            logger.info(f"{self.type_of}: Tapping on element by locator {self.locator}")
            el = self.wait_for_element()
            el.click()

    def is_displayed(self) -> bool:
        try:
            el = self.wait_for_element()
            return el.is_displayed()
        except Exception:
            return False

    def should_be_visible(self, timeout=None):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            try:
                el = self.wait_for_element(timeout=timeout)
                assert el.is_displayed(), f'{self.name} is not visible'
            except StaleElementReferenceException:
                self.should_be_visible(timeout=timeout)

    def get_text(self):
        with allure.step(f'Getting text from {self.type_of} "{self.name}"'):
            el = self.wait_for_element()
            return el.text

    def should_have_text(self, expected_text: str):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{expected_text}"'):
            el = self.wait_for_element()
            actual = el.text
            assert actual == expected_text, f'Expected "{expected_text}", got "{actual}"'

    def fill(self, text: str):
        with allure.step(f'Setting text "{text}" to {self.type_of} "{self.name}"'):
            el = self.wait_for_element()
            el.clear()
            el.send_keys(text)
