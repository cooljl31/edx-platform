"""
Signup page for studio
"""
from bok_choy.page_object import PageObject

from . import BASE_URL
from common.test.acceptance.pages.studio.utils import set_input_value
from common.test.acceptance.pages.common.utils import click_css


class SignupPage(PageObject):
    """
    Signup page for Studio.
    """

    url = BASE_URL + "/signup"

    def is_browser_on_page(self):
        return self.q(css='body.view-signup').present

    def sign_up_user(self, registration_dictionary):
        """
        Register the user.
        """
        for css, value in registration_dictionary.iteritems():
            set_input_value(self, css, value)

        click_css(page=self, css='#tos', require_notification=False)
        click_css(page=self, css='#submit', require_notification=False)
