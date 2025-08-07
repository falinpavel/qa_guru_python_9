# ЧАСТЬ I (реализовано в бренче mid-level-step-objects)
## Реализованные тесты, где бизнес шаги пользователя описаны подробно по каждому полю формы
```python
    def test_successful_filling_table_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.type_first_name(first_name='Elena')
        practice_form_page.type_last_name(last_name='Sidorova')
        practice_form_page.type_user_email(user_email='Elena123@example.com')
        practice_form_page.choose_gender('Female')
        practice_form_page.send_keys_user_number(user_number='8800255612')
        practice_form_page.enable_date_of_birth()
        practice_form_page.type_subjects('Maths', 'English')
        practice_form_page.choose_hobbies('Music')
        practice_form_page.upload_file()
        practice_form_page.type_current_address(address='Krasnodar')
        practice_form_page.choose_state_and_city()
        practice_form_page.submit_form()
        practice_form_page.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)
        practice_form_page.should_table_be_filled(
            full_name='Elena Sidorova',
            user_email='Elena123@example.com',
            gender='Female',
            user_number='8800255612',
            date_of_birth='23 May,1996',
            subjects='Maths, English',
            hobbies='Music',
            file='file.txt',
            current_address='Krasnodar',
            state_and_city='Uttar Pradesh Lucknow'
        )
```
# ЧАСТЬ II (реализовано в бренче high-level-step-objects)
## Реализованные тесты, где бизнес шаги пользователя инкапсулированы в отдельные большие методы и спрятаны в классах
```python
class TestPracticeForm:

    def test_success_submission_practice_form(self, practice_form_page):
        practice_form_page.open_page().registration_random_user_and_submit_form()

    def test_successful_filling_table_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.registration_random_user_and_submit_form()
        practice_form_page.should_that_table_be_filled()

    def test_submission_form_with_empty_fields(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.form_not_filled_and_not_submitted()

    def test_check_texts_on_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.should_all_texts_into_form()
```
# Часть III – (реализовано в бренче application-manager)