import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa.utils import attachments


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    """Настройка драйвера"""
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    """Создание драйвера"""
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    """Передача драйвера в Selene"""
    browser.config.driver = driver

    """Настройка браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield browser

    """Добавление аттачей к тесту"""
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_html(browser)
    attachments.add_video(browser)

    browser.quit()