from selene import browser, be, have


class LeftPanel:

    @staticmethod
    def go_to_elements_text_box():
        browser.all('.element-group').element_by(have.exact_text('Elements')).click()
        browser.element('#item-0').element_by(have.exact_text('Text Box')).click()
