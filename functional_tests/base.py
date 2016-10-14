from selenium import webdriver
import os
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super(FunctionalTest, cls).setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(FunctionalTest, cls).tearDownClass()

    def setUp(self):
        chromedriver = r'C:\Users\Oluwafemi\Downloads\chromedriver_win32\chromedriver'
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(1)

    def tearDown(self):
        #time.sleep(10)
        self.browser.refresh()
        self.browser.quit()

    def check_for_row_in_list(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')    
