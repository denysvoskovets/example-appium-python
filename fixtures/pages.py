import pytest

from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage
from pages.profile_page import ProfilePage


@pytest.fixture()
def onboarding_page(driver) -> OnboardingPage:
    return OnboardingPage(driver)


@pytest.fixture()
def main_page(driver_with_state) -> MainPage:
    return MainPage(driver_with_state)


@pytest.fixture()
def profile_page(driver_with_state) -> ProfilePage:
    return ProfilePage(driver_with_state)
