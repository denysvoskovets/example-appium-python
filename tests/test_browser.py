from selenium.webdriver.common.by import By


def test_open_site(chrome_driver):
    chrome_driver.get("https://promova.com/")
    chrome_driver.find_element(By.CSS_SELECTOR, 'button[aria-label="side navigation"]').click()

    assert chrome_driver.find_element(By.CSS_SELECTOR, '.navigation_actions_login__upHvk')
