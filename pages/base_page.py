from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import allure

from utils.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @property
    def type_of(self) -> str:
        return "base element"

    def wait_for_element(self, by, locator, condition=EC.presence_of_element_located, timeout=None):
        timeout = timeout or self.timeout
        logger.info(f"Waiting for element by {by}='{locator}' with timeout {timeout}s")
        return WebDriverWait(self.driver, timeout).until(
            condition((by, locator))
        )

    def wait_for_all_elements(self, by, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, locator))
        )

    def click(self, by, locator):
        element = self.wait_for_element(by, locator, condition=EC.element_to_be_clickable)
        step = f'{self.type_of}: Tapping on element by locator ({by}, {locator})'
        with allure.step(step):
            logger.info(step)
            element.click()

    def scroll_vertically(self, direction='down', duration=300):
        step = f'Scrolling vertically with direction {direction}'
        with allure.step(step):
            screen_size = self.driver.get_window_size()
            start_x = screen_size['width'] / 2
            start_y = screen_size['height'] * (0.8 if direction == 'down' else 0.2)
            end_y = screen_size['height'] * (0.2 if direction == 'down' else 0.8)

            actions = ActionChains(self.driver)
            finger = PointerInput(interaction.POINTER_TOUCH, "finger")
            action_builder = ActionBuilder(self.driver, mouse=finger)

            logger.info(step)
            action_builder.pointer_action.move_to_location(int(start_x), int(start_y))
            action_builder.pointer_action.pointer_down()
            action_builder.pointer_action.pause(duration / 1000)
            action_builder.pointer_action.move_to_location(int(start_x), int(end_y))
            action_builder.pointer_action.pointer_up()

            actions.w3c_actions = action_builder
            actions.perform()
