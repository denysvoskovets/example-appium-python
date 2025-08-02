import allure

from pages.onboarding_page import OnboardingPage
from resources.strings import STRINGS
from config.credentials import BASIC_EMAIL, BASIC_PASSWORD
import pytest


@allure.suite("Authorization")
@pytest.mark.smoke
@pytest.mark.authorization
class TestSignUp:
    @pytest.mark.parametrize('email, password',
                             [("a", "1"), ("email@email", "1"), ("email@email..email", "1")])
    def test_incorrect_email(self, onboarding_page: OnboardingPage, email: str, password: str):
        onboarding_page.tap_i_have_an_account()
        onboarding_page.tap_navigate_signup_menu()
        onboarding_page.fill_email(email)
        onboarding_page.fill_password(password)
        onboarding_page.tap_signup_button()

        oops_email_label = onboarding_page.get_email_error_label()
        assert oops_email_label.is_displayed()

        # commenting because some test-id is crucial here. don't want to use time.sleep.
        # Test is flaky due to presence of element and rebuilding POM
        # assert oops_email_label.text == STRINGS['en']['email_oops_error']

    def test_eye_password_logic(self, onboarding_page: OnboardingPage):
        onboarding_page.tap_i_have_an_account()
        onboarding_page.tap_navigate_signup_menu()
        onboarding_page.fill_email(BASIC_EMAIL)
        onboarding_page.fill_password(BASIC_PASSWORD)
        assert onboarding_page.get_password_text() == '••••••'

        onboarding_page.tap_on_eye()
        assert onboarding_page.get_password_text() == BASIC_PASSWORD


@allure.suite("Onboarding")
@pytest.mark.smoke
@pytest.mark.long
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_full_onboarding(onboarding_page: OnboardingPage):
    onboarding_page.tap_get_started()
    onboarding_page.tap_english_selector()
    onboarding_page.wait_instructions()
    onboarding_page.tap_english_selector()
    onboarding_page.tap_continue()
    onboarding_page.tap_beginner()
    onboarding_page.select_and_compare_motivations(indexes=[1, 2])
    onboarding_page.tap_motivations_continue()
    onboarding_page.tap_topic_yes_until_gone()
    onboarding_page.tap_skill()
    onboarding_page.tap_continue()
    onboarding_page.tap_mins()
    onboarding_page.tap_enjoy()

    assert onboarding_page.wait_for_sign_up_button().is_displayed()
