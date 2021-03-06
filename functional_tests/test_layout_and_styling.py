from selenium import webdriver
import os
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class LayoutAndStyling(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the Home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # she notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width']/2,
        512,
        delta=10
        )

        # She starts a new list and sees that the input is nicely
        # centered too
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width']/2,
        512,
        delta=10
        )
