# ЧАСТЬ I (реализовано в бренче mid-level-step-objects)
## Реализованные тесты, где бизнес шаги пользователя описаны подробно по каждому полю формы
### Тесты:
```python
class TestPracticeForm(PracticeFormPage):

    def test_success_submission_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.type_first_name(first_name='Ivan')
        practice_form_page.type_last_name(last_name='Ivanov')
        practice_form_page.type_user_email(user_email='test@example.com')
        practice_form_page.choose_gender('Male')
        practice_form_page.send_keys_user_number(user_number='8800255653')
        practice_form_page.enable_date_of_birth()
        practice_form_page.type_subjects('Computer Science')
        practice_form_page.choose_hobbies('Sports')
        practice_form_page.upload_file()
        practice_form_page.type_current_address(address='Moscow')
        practice_form_page.choose_state_and_city()
        practice_form_page.submit_form()
        practice_form_page.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)
```
# ЧАСТЬ II (реализовано в бренче high-level-step-objects)
## Реализованные тесты, где бизнес шаги пользователя инкапсулированы в отдельные большие методы и спрятаны в классах
### Тесты:
```python
class TestPracticeForm:

    def test_success_submission_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.registration_random_user_and_submit_form()
        practice_form_page.should_that_table_be_filled()
```
# Часть III – (реализовано в бренче application-manager)
### Тесты:
```python
from tests.application_manager.application_manager import demoqa


class TestPracticeForm:
    
    def test_registration_practice_form_and_go_to_registration_text_box_page(self):
        demoqa.page_practice_form.open_page()
        demoqa.page_practice_form.registration_random_user_and_submit_form()
        demoqa.page_practice_form.should_that_table_be_filled()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_elements()
        demoqa.left_panel_elements.click_to_text_box()
        demoqa.page_text_box.registration_random_user_and_submit_form().should_all_values_after_submit()
```
### Реализация application-manager:
```python
from pages.elements.text_box.page_text_box import TextBoxPage
from pages.forms.practice_form.page_practice_form import PracticeFormPage
from pages.teft_panel.left_panel import LeftPanel, LeftPanelElements, LeftPanelForms


class ApplicationManager:

    def __init__(self):

        self.page_practice_form = PracticeFormPage()
        self.page_text_box = TextBoxPage()

        self.left_panel = LeftPanel()
        self.left_panel_elements = LeftPanelElements()
        self.left_panel_forms = LeftPanelForms()


demoqa = ApplicationManager()
```