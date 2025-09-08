import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name="screenshot", attachment_type=AttachmentType.PNG, extension=".png")


def add_logs(browser):
    try:
        logs = "".join(f"{text}\n" for text in browser.driver.get_log(log_type="browser"))
    except AttributeError:
        logs = "Browser logs are not available because the get_log method does not exist in your version of Selenium."
    allure.attach(logs, "browser_logs", AttachmentType.TEXT, ".log")


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, "page_source", AttachmentType.HTML, ".html")