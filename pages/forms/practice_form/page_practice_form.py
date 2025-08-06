from datetime import datetime
from selene import browser, be, have
from const import UPLOADED_FILE
from data.user_info import UsersForTests as Users


class PracticeFormPage:

    URL = '/automation-practice-form'

    user = Users().choose_random_user()
    print(user)

    def open_page(self) -> browser:
        browser.open(self.URL)

    def registration_random_user_and_submit_form(self) -> None:
        browser.element('#firstName').should(be.blank).type(self.user.first_name).should(be.not_.blank).should(
            have.attribute("value").value(self.user.first_name))
        browser.element('#lastName').should(be.blank).type(self.user.last_name).should(be.not_.blank).should(
            have.attribute("value").value(self.user.last_name))
        browser.element('#userEmail').should(be.blank).type(self.user.user_email).should(be.not_.blank).should(
            have.attribute("value").value(self.user.user_email))
        browser.all('[class="custom-control-label"]').element_by(
            have.text(self.user.gender)).click().should(be.enabled)
        browser.element('#userNumber').should(be.blank).send_keys(self.user.user_number).should(
            be.not_.blank).should(have.attribute("value").value(self.user.user_number))
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().all('[value]').element_by(
            have.text(self.user.birth_month)).click()
        browser.element('.react-datepicker__year-select').click().all('[value]').element_by(
            have.attribute("value").value(self.user.birth_year)).click()
        browser.element('.react-datepicker__month').click().all('[role="option"]').element_by(
            have.text(self.user.birth_day)).click()
        browser.element('#dateOfBirthInput').should(be.not_.blank).should(have.attribute("value").value(
            f'{int(self.user.birth_day):02d} {self.user.birth_month[:3]} {self.user.birth_year}'))
        for subject in self.user.subjects:
            browser.element('#subjectsInput').type(subject).press_enter()
        for hobby in self.user.hobbies:
            browser.all('label[class="custom-control-label"]').element_by(
                have.text(hobby)).click().should(be.enabled)
        browser.element('#uploadPicture').send_keys(UPLOADED_FILE)
        browser.element('#currentAddress').should(be.blank).type(self.user.current_address).should(
            be.not_.blank).should(have.attribute("value").value(self.user.current_address))
        browser.element('#state').click().all('[tabindex="-1"]').element_by(have.text(self.user.state)).click()
        browser.element('#city').click().all('[tabindex="-1"]').element_by(have.text(self.user.city)).click()
        browser.element('#submit').should(be.clickable).click()

    def should_that_table_be_filled(self) -> None:
        table_element = browser.all('table.table-dark tbody tr')
        table_element.element_by(have.text('Student Name')).all('td').second.should(
            have.text(f"{self.user.first_name} {self.user.last_name}"))
        table_element.element_by(have.text('Student Email')).all('td').second.should(
            have.text(self.user.user_email))
        table_element.element_by(have.text('Gender')).all('td').second.should(have.text(self.user.gender))
        table_element.element_by(have.text('Mobile')).all('td').second.should(have.text(self.user.user_number))
        table_element.element_by(have.text('Date of Birth')).all('td').second.should(
            have.text(f'{self.user.birth_day} {self.user.birth_month},{self.user.birth_year}'))
        table_element.element_by(have.text('Subjects')).all('td').second.should(
            have.text(', '.join(self.user.subjects)))
        table_element.element_by(have.text('Hobbies')).all('td').second.should(
            have.text(', '.join(self.user.hobbies)))
        table_element.element_by(have.text('Picture')).all('td').second.should(have.text("file.txt"))
        table_element.element_by(have.text('Address')).all('td').second.should(
            have.text(self.user.current_address))
        table_element.element_by(have.text('State and City')).all('td').second.should(
            have.text(f"{self.user.state} {self.user.city}"))

    @staticmethod
    def should_all_texts_into_form() -> None:
        browser.element('.text-center').should(have.text('Practice Form'))
        browser.element('.practice-form-wrapper h5').should(have.text('Student Registration Form'))
        browser.element('#userName-wrapper').should(have.exact_text('Name'))
        browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
        browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
        browser.element('#genterWrapper').should(have.text('Gender'))
        browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
        browser.element('#userNumber-label').should(have.text('Mobile')).element('small').should(
            have.text('(10 Digits)'))
        browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
        browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
        browser.element('#dateOfBirthInput').should(have.attribute('value').value(datetime.now().strftime('%d %b %Y')))
        browser.element('#subjectsWrapper').should(have.text('Subjects'))
        browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
        browser.all('.custom-checkbox').should(have.size(3)).should(have.exact_texts('Sports', 'Reading', 'Music'))
        browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
        browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
        browser.element('#stateCity-wrapper').should(have.text('State and City'))

    @staticmethod
    def form_not_filled_and_not_submitted() -> None:
        browser.element('#submit').click()
        # browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-title').should(be.not_.present)
