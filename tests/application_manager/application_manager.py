from pages.elements.text_box.page_text_box import TextBoxPage
from pages.forms.practice_form.page_practice_form import PracticeFormPage
from pages.teft_panel.left_panel import LeftPanel


class ApplicationManager:

    left_panel = LeftPanel()
    page_text_box: TextBoxPage()
    page_practice_form: PracticeFormPage()

    def __init__(self):
        self.page_practice_form = PracticeFormPage()
        self.page_text_box = TextBoxPage()
        self.left_panel = LeftPanel()


demoqa = ApplicationManager()
