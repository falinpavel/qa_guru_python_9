from tests.application_manager.application_manager import demoqa


class TestNavigateOnLeftPanel:
    def test_navigate_on_left_panel(self):
        demoqa.page_practice_form.open_page()
        demoqa.left_panel.go_to_elements_text_box()
