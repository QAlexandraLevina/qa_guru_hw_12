import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa.utils import attachments

@pytest.fixture(scope='function', autouse=True)
def configuration_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://demoqa.com/automation-practice-form")
    browser.config.timeout = 10

    yield

    browser.quit()