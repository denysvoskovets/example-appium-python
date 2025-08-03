from appium.webdriver.common.appiumby import AppiumBy

TROPHY_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[1]'),
    "ios": None
}

FIRE_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[2]'),
    "ios": None
}

PROFILE_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Get premium to unlock all units"]/../following-sibling::android.view.View[3]'),
    "ios": None
}

PROFILE_NAV_BUTTON = {
    "android": (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()]'),
    "ios": None
}

TUTORS_NAV_BUTTON = {
    "android": (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-1]'),
    "ios": None
}

FOR_YOU_NAV_BUTTON = {
    "android": (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-2]'),
    "ios": None
}

MY_PLAN_NAV_BUTTON = {
    "android": (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[last()-3]'),
    "ios": None
}

CURRENT_LEVEL = {
    "android": (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.TextView'),
    "ios": None
}
