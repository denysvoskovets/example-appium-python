import os

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

APP_PACKAGE = "com.appsci.tenwords"
CHROMEDRIVER_PATH = os.path.abspath("utils/chromeDriver/chromedriver")


def get_android_options(no_reset=False):
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        "appium:deviceName": "Pixel 9",
        "appium:appPackage": APP_PACKAGE,
        "appium:appActivity": "com.appsci.words.Launcher",
        "appium:autoGrantPermissions": "true",
        "appium:noReset": str(no_reset).lower(),
        # "appium:newCommandTimeout": 300
    }
    return UiAutomator2Options().load_capabilities(capabilities)


def get_android_chrome_options(device_name="Pixel 9", no_reset=False):
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        "appium:deviceName": device_name,
        "appium:browserName": "Chrome",
        "appium:chromedriverAutodownload": True,
        "appium:noReset": str(no_reset).lower(),
        "appium:chromedriverExecutable": CHROMEDRIVER_PATH,
    }
    return UiAutomator2Options().load_capabilities(capabilities)


def get_ios_options(device_name="iPhone Simulator", no_reset=False):
    capabilities = {
        "platformName": "iOS",
        "appium:automationName": "XCUITest",
        "appium:deviceName": device_name,
        "appium:platformVersion": "16.4",
        "appium:bundleId": APP_PACKAGE,
        "appium:noReset": str(no_reset).lower(),
        "appium:autoAcceptAlerts": True,
    }
    return XCUITestOptions().load_capabilities(capabilities)


def get_driver_options(platform, device_name, no_reset=False):
    if platform.lower() == "android":
        return get_android_options(no_reset=no_reset)
    elif platform.lower() == "ios":
        return get_ios_options(device_name=device_name, no_reset=no_reset)
    else:
        raise ValueError(f"Unsupported platform: {platform}")


def get_appium_server_url():
    return 'http://localhost:4723'
