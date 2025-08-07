from selene import browser, be, have


class LeftPanel:

    def go_to_elements_text_box(self, to):
        browser.all('.element-group .header-text').element_by(have.text(to)).click()
        # browser.element('#item-0').element_by(have.exact_text('Text Box')).click()
