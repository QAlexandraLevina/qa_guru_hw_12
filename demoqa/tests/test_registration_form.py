import allure
from selene.support.shared import browser
from demoqa.pages.registration_page import RegistrationPage
from demoqa.users import UserData


@allure.title("Успешное заполнение формы")
def test_field_practice_form(setup_browser):
    """Инициализация экземпляров класса RegistrationPage и UserData"""
    alexandra = UserData(
        "Alexandra",
        "Levina",
        "alexandralevina1@gmail.com",
        "Female",
        "8912345678",
        ("February", "2002", "17"),
        "Computer Science",
        ("Sports", "Reading", "Music"),
        "test_file.txt",
        "Россия, г.Москва, ул.Маршала Жукова 1",
        ("NCR", "Delhi"),
    )

    registration_page = RegistrationPage()

    with allure.step("Открытие страницы с формой"):
        browser.open("https://demoqa.com/automation-practice-form")


    with allure.step("Заполнение формы"):
        browser.execute_script("window.scrollBy(0, 500)")
        registration_page.completing_practice_form_fields(alexandra)


    with allure.step("Проверка заполненной формы"):
        registration_page.should_completed_practice_form(alexandra)


    with allure.step("Закрытие модального окна"):
        registration_page.button_close.click()