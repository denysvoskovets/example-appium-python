import os

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv

from config.capabilities import get_android_chrome_options, get_driver_options
import allure
import pytest
from appium import webdriver
from config.capabilities import get_appium_server_url, APP_PACKAGE
from config.credentials import VALID_EMAIL_FIXTURE, VALID_PASS_FIXTURE
from pages.onboarding_page import OnboardingPage
from utils.cleanup import clear_screenshots_folder
from datetime import datetime

load_dotenv()

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
BROWSERSTACK_SERVER_URL = f"http://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub"


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment: dev/stage/prod")
    parser.addoption("--platform", action="store", default="android", help="android or ios")
    parser.addoption("--device", action="store", default="Pixel 9", help="Device name or simulator name")
    parser.addoption("--browserstack", action="store_true", help="Run tests on BrowserStack")


@pytest.fixture(scope="session")
def cli_options(request):
    return {
        "env": request.config.getoption("--env") or "dev",
        "platform": request.config.getoption("--platform") or "android",
        "device": request.config.getoption("--device") or "Pixel 9",
        "browserstack": request.config.getoption("--browserstack"),
    }


def create_driver(platform, device, no_reset=False, use_browserstack=False):
    if use_browserstack:
        if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
            raise RuntimeError("BrowserStack credentials are not set in environment variables.")

        capabilities = {
            "platformName": platform,
            "deviceName": device,
            "automationName": "uiautomator2" if platform.lower() == "android" else "XCUITest",
            "app": "bs://<your-app-id-on-browserstack>",
            "project": "My Project",
            "build": "build-1",
            "name": "Sample Test",
            "noReset": no_reset,
            "browserstack.debug": True,
        }

        if platform.lower() == "android":
            options = UiAutomator2Options().load_capabilities(capabilities)
        else:
            options = XCUITestOptions().load_capabilities(capabilities)

        driver = webdriver.Remote(BROWSERSTACK_SERVER_URL, options=options)

    else:
        options = get_driver_options(platform=platform, device_name=device, no_reset=no_reset)
        appium_url = get_appium_server_url()
        driver = webdriver.Remote(appium_url, options=options)

    return driver


@pytest.fixture()
def driver(cli_options):
    driver = create_driver(
        platform=cli_options["platform"],
        device=cli_options["device"],
        no_reset=False,
        use_browserstack=cli_options["browserstack"],
    )
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def initialize_driver_state(cli_options):
    driver = create_driver(
        platform=cli_options["platform"],
        device=cli_options["device"],
        no_reset=False,
        use_browserstack=cli_options["browserstack"],
    )

    onboarding = OnboardingPage(driver)
    onboarding.tap_i_have_an_account()
    onboarding.fill_email(VALID_EMAIL_FIXTURE)
    onboarding.fill_password(VALID_PASS_FIXTURE)
    onboarding.tap_login_button()
    onboarding.setting_account_label.is_displayed()

    driver.quit()


@pytest.fixture()
def driver_with_state(cli_options, initialize_driver_state):
    driver = create_driver(
        platform=cli_options["platform"],
        device=cli_options["device"],
        no_reset=True,
        use_browserstack=cli_options["browserstack"],
    )

    if cli_options["platform"].lower() == "android" and not cli_options["browserstack"]:
        driver.activate_app(APP_PACKAGE)

    yield driver

    if cli_options["platform"].lower() == "android" and not cli_options["browserstack"]:
        driver.terminate_app(APP_PACKAGE)

    driver.quit()


@pytest.fixture()
def chrome_driver(cli_options):
    if cli_options["platform"].lower() != "android":
        raise ValueError("Chrome driver is only supported on Android.")

    options = get_android_chrome_options(
        device_name=cli_options["device"],
    )
    appium_url = get_appium_server_url()
    driver = webdriver.Remote(appium_url, options=options)
    yield driver
    driver.quit()


def pytest_sessionstart(session):
    clear_screenshots_folder()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item._request.node, "_driver", None)
        if driver:
            path = "utils/screenshots/fail_screenshots"
            os.makedirs(path, exist_ok=True)

            test_name = item.nodeid.replace("/", "_").replace("::", "_")
            filename = os.path.join(path, f"{test_name}_{datetime.now():%Y-%m-%d_%H-%M-%S}.png")

            try:
                driver.save_screenshot(filename)
                allure.attach.file(filename, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Screenshot error: {e}")
