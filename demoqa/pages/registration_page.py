from demoqa.users import UserData
import os
from selene import browser, by, have


class RegistrationPage:
    """Инициализация атрибутов с локаторами элементов формы"""
    def __init__(self):
        self.field_first_name = browser.element("#firstName")
        self.field_last_name = browser.element("#lastName")
        self.field_email = browser.element("#userEmail")
        self.field_gender = browser.element("#genterWrapper")
        self.field_mobile = browser.element("#userNumber")
        self.field_date_of_birth = browser.element("#dateOfBirthInput")
        self.field_month_of_birth = browser.all(".react-datepicker__month-select option")
        self.field_year_of_birth = browser.all(".react-datepicker__year-select option")
        self.field_day_of_birth = browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)")
        self.field_subjects = browser.element("#subjectsInput")
        self.field_hobbies = browser.element("#hobbiesWrapper")
        self.field_picture = browser.element("#uploadPicture")
        self.field_current_address = browser.element("#currentAddress")
        self.field_state = browser.element("#state")
        self.field_city = browser.element("#city")
        self.button_submit = browser.element("#submit")
        self.completed_registration_form = browser.all("tbody tr td:nth-child(2)")
        self.button_close = browser.element("#closeLargeModal")

    """Заполнение поля Date of Birth"""
    def fill_field_date_of_birth(self, month, year, day):
        self.field_date_of_birth.click()
        self.field_month_of_birth.element_by(have.exact_text(month)).click()
        self.field_year_of_birth.element_by(have.exact_text(year)).click()
        self.field_day_of_birth.element_by(have.exact_text(day)).click()
        return self


    """Выбор чек-боксов Hobbies"""
    def set_hobbies(self, tuple_hobbies):
        for hobb in tuple_hobbies:
            self.field_hobbies.element(by.text(hobb)).click()
        return self


    """Выбор State and City"""
    def set_state_and_city(self, tuple_state_city):
        state, city = tuple_state_city
        self.field_state.click()
        browser.element(by.text(state)).click()
        self.field_city.click()
        browser.element(by.text(city)).click()
        return self


    """Проверка заполненной формы"""
    def should_completed_practice_form(self, user: UserData):
        self.completed_registration_form.should(
            have.exact_texts(
                user.full_name,
                user.email,
                user.gender,
                user.mobile,
                user.birthday,
                user.subjects,
                user.hobby,
                user.picture,
                user.current_address,
                user.state_n_city
            )
        )
        return self


    """Заполнение полей формы регистрации"""
    def completing_practice_form_fields(self, user: UserData):
        self.field_first_name.type(user.first_name)
        self.field_last_name.type(user.last_name)
        self.field_email.type(user.email)
        self.field_gender.element(by.text(user.gender)).click()
        self.field_mobile.type(user.mobile)
        self.fill_field_date_of_birth(*user.date_of_birth)
        self.field_subjects.type(user.subjects).press_enter()
        self.set_hobbies(user.hobbies)
        self.field_picture.send_keys(os.path.join(os.path.dirname(__file__), "test_file.txt"))
        self.field_current_address.type(user.current_address)
        self.set_state_and_city(user.state_and_city)
        self.button_submit.click()