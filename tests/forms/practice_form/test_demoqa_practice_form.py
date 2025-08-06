from pages.forms.practice_form.page_practice_form import PracticeFormPage


class TestPracticeForm(PracticeFormPage):

    def test_success_submission_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.registration_random_user_and_submit_form()

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
