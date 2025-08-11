from datetime import datetime

from selene import browser, be, have, command

from const import UPLOADED_FILE


class PracticeFormPage:

    URL = '/automation-practice-form'

    def open_page(self):
        browser.open(self.URL)
        return self

    def registration_random_user_and_submit_form(self, user) -> 'PracticeFormPage':
        browser.element('#firstName').should(be.blank).type(user.first_name).should(be.not_.blank).should(
            have.attribute("value").value(user.first_name))
        browser.element('#lastName').should(be.blank).type(user.last_name).should(be.not_.blank).should(
            have.attribute("value").value(user.last_name))
        browser.element('#userEmail').should(be.blank).type(user.user_email).should(be.not_.blank).should(
            have.attribute("value").value(user.user_email))
        browser.all('.custom-radio').element_by(
            have.text(user.gender)).click().should(be.enabled)
        browser.element('#userNumber').should(be.blank).send_keys(user.user_number).should(
            be.not_.blank).should(have.attribute("value").value(user.user_number))
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').should(be.visible).click().all('[value]').element_by(
            have.text(user.birth_month)).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click().all('[value]').element_by(
            have.attribute("value").value(user.birth_year)).click()
        browser.element('[class=react-datepicker__month][role="listbox"]').should(
            be.visible).click().all('div[role="option"]').element_by(have.text(user.birth_day)).click()
        browser.element('#dateOfBirthInput').should(be.visible).should(have.attribute("value").value(
            f'{int(user.birth_day):02d} {user.birth_month[:3]} {user.birth_year}'))
        for subject in user.subjects:
            browser.element('#subjectsInput').should(be.visible).type(subject).press_enter()
        for hobby in user.hobbies:
            browser.all('.custom-checkbox').element_by(have.text(hobby)).click().should(be.enabled)
        browser.element('#uploadPicture').perform(command.js.scroll_into_view).send_keys(UPLOADED_FILE)
        browser.element('#currentAddress').should(be.visible).should(be.blank).type(user.current_address).should(
            be.not_.blank).should(have.attribute("value").value(user.current_address))
        browser.element('#state').click().all('[tabindex="-1"]').element_by(have.text(user.state)).click()
        browser.element('#city').click().all('[tabindex="-1"]').element_by(have.text(user.city)).click()
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    def should_that_table_be_filled(self, user) -> 'PracticeFormPage':
        table_element = browser.all('table.table-dark tbody tr')
        table_element.element_by(have.text('Student Name')).all('td').second.should(
            have.text(f"{user.first_name} {user.last_name}"))
        table_element.element_by(have.text('Student Email')).all('td').second.should(
            have.text(user.user_email))
        table_element.element_by(have.text('Gender')).all('td').second.should(have.text(user.gender))
        table_element.element_by(have.text('Mobile')).all('td').second.should(have.text(user.user_number))
        table_element.element_by(have.text('Date of Birth')).all('td').second.should(
            have.text(f'{user.birth_day} {user.birth_month},{user.birth_year}'))
        table_element.element_by(have.text('Subjects')).all('td').second.should(
            have.text(', '.join(user.subjects)))
        table_element.element_by(have.text('Hobbies')).all('td').second.should(
            have.text(', '.join(user.hobbies)))
        table_element.element_by(have.text('Picture')).all('td').second.should(have.text("file.txt"))
        table_element.element_by(have.text('Address')).all('td').second.should(
            have.text(user.current_address))
        table_element.element_by(have.text('State and City')).all('td').second.should(
            have.text(f"{user.state} {user.city}"))
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).should(be.clickable).click()
        return self

    def should_all_texts_into_form(self) -> 'PracticeFormPage':
        browser.element('.text-center').should(have.text('Practice Form'))
        browser.element('.practice-form-wrapper h5').should(have.text('Student Registration Form'))
        browser.element('#userName-wrapper').should(have.exact_text('Name'))
        browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
        browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
        browser.element('#genterWrapper').perform(command.js.scroll_into_view).should(have.text('Gender'))
        browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
        browser.element('#userNumber-label').should(have.text('Mobile')).element('small').should(
            have.text('(10 Digits)'))
        browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
        browser.element('#dateOfBirth-label').perform(command.js.scroll_into_view).should(have.text('Date of Birth'))
        browser.element('#dateOfBirthInput').should(have.attribute('value').value(datetime.now().strftime('%d %b %Y')))
        browser.element('#subjectsWrapper').should(have.text('Subjects'))
        browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
        browser.all('.custom-checkbox').should(have.size(3)).should(have.exact_texts('Sports', 'Reading', 'Music'))
        browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
        browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
        browser.element('#stateCity-wrapper').perform(command.js.scroll_into_view).should(have.text('State and City'))
        return self

    def form_not_filled_and_not_submitted(self) -> 'PracticeFormPage':
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        # browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-title').should(be.not_.present)
        return self


practice_form_page = PracticeFormPage()
