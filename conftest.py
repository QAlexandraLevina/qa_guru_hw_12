import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa.utils import attachments


def pytest_addoption(parser):
    """Настройка параметров для браузера"""
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


@pytest.fixture(scope="session", autouse=True)
def setup_browser(request):
    """Получение информации о значении параметра browser из командной строки"""
    browser_version = request.config.getoption('--browser_version')

    """Настройка драйвера"""
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
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

    """Настройка параметров браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 20

    yield browser

    """Добавление аттачей к тесту"""
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_html(browser)
    attachments.add_video(browser)

    browser.quit()