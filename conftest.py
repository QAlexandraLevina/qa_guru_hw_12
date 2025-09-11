import os

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa.utils import attachments
from dotenv import load_dotenv


DEFAULT_BROWSER_VERSION = "128.0"

def pytest_addoption(parser):
    """Настройка параметров для браузера"""
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Загрузка переменных сред из файла .env"""
    load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def setup_browser(request):
    """Получение информации о значении параметра browser из командной строки"""
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

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
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
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