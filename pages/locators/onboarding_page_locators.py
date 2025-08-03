from appium.webdriver.common.appiumby import AppiumBy

GET_STARTED_BUTTON = {
    "android": (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").childSelector(new UiSelector().text("GET STARTED"))'),
    "ios": None
}

I_HAVE_AN_ACCOUNT_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.view.View[./android.widget.TextView[@text="I HAVE AN ACCOUNT"]]'),
    "ios": None
}

LOG_IN_TEXT = {
    "android": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")'),
    "ios": None
}

SIGN_UP_TEXT = {
    "android": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")'),
    "ios": None
}

SIGN_UP_NAV_BUTTON = {
    "android": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")'),
    "ios": None
}

EMAIL_FIELD = {
    "android": (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]'),
    "ios": None
}

PASSWORD_FIELD = {
    "android": (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]'),
    "ios": None
}

PASSWORD_EYE_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]/android.view.View'),
    "ios": None
}

LOGIN_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="LOG IN"]'),
    "ios": None
}

SIGN_UP_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="SIGN UP"]'),
    "ios": None
}

OOPS_LABEL = {
    "android": (AppiumBy.XPATH,
                '//android.widget.ScrollView/android.widget.EditText[1]/following-sibling::android.widget.TextView[1]'),
    "ios": None
}

WRONG_PASSWORD_LABEL = {
    "android": (AppiumBy.XPATH,
                '//android.widget.ScrollView/android.widget.EditText[2]/following-sibling::android.widget.TextView'),
    "ios": None
}

SETTING_ACCOUNT_LABEL = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Setting up your learning experience"]'),
    "ios": None
}

ENGLISH_SELECTOR = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="English"]'),
    "ios": None
}

INSTRUCTIONS_LABEL = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Instructions should be in:"]'),
    "ios": None
}

CONTINUE_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]'),
    "ios": None
}

BEGINNER_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Beginner"]'),
    "ios": None
}

MOTIVATION_ELEMENTS = {
    "android": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View'),
    "ios": None
}

MOTIVATION_CONTINUE_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]'),
    "ios": None
}

TOPIC_YES_BUTTON = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="YES"]/preceding-sibling::android.view.View[2]'),
    "ios": None
}

GRAMMAR_SKILL = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Grammar"]'),
    "ios": None
}

FIVE_MINS_ELEMENT = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="5 min"]'),
    "ios": None
}

ENJOY_LABEL = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Enjoyed by 10M people"]'),
    "ios": None
}

SIGN_UP_WITH_EMAIL = {
    "android": (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up with email"]'),
    "ios": None
}