import pytest

from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@pytest.mark.smoke
def test_current_level(main_page: MainPage):
    main_page.wait_until_loaded(timeout=15)
    main_page.scroll_up()
    assert main_page.get_current_level().is_displayed()


@pytest.mark.smoke
def test_navigate_to_profile(main_page: MainPage, profile_page: ProfilePage):
    main_page.wait_until_loaded(timeout=15)
    main_page.open_profile()
    assert profile_page.get_ukrainians_button().is_displayed()
