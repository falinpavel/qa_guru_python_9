from data.user_info import User
from helpers.pages.forms.practice_form.page_practice_form import practice_form_page


class TestPracticeForm:

    def test_success_submission_practice_form(self):
        practice_form_page.open_page()
        user = User()
        practice_form_page.registration_random_user_and_submit_form(user=user)

    def test_successful_filling_table_practice_form(self):
        practice_form_page.open_page()
        user = User()
        practice_form_page.registration_random_user_and_submit_form(user=user)
        practice_form_page.should_that_table_be_filled(user=user)

    def test_submission_form_with_empty_fields(self):
        practice_form_page.open_page()
        practice_form_page.form_not_filled_and_not_submitted()

    def test_check_texts_on_form(self):
        practice_form_page.open_page()
        practice_form_page.should_all_texts_into_form()
