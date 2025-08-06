from selene import browser, be, have

from config.links import Links


class TextBoxPage:

    URL = Links.TEXT_BOX

    def open_page(self):
        browser.open(self.URL)
        return self
