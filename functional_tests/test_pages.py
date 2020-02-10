from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestPagesApp(StaticLiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
    self.browser.maximize_window()
    self.browser.get(self.live_server_url) # 'http://127.0.0.1:8000/'

  def tearDown(self):
    self.browser.close()

  def test_home_page_loaded(self):
    home_header = self.browser.find_elements_by_css_selector('#home')
    self.assertNotEqual(len(home_header), 0, 'Home header element was not found')
    
  def test_redirected_to_register_page(self):
    # Get register button
    register_btn = self.browser.find_element_by_xpath('//*[@id="home"]/div/div/div/a')
    # Click the button
    register_btn.click()

    current_url = self.browser.current_url
    register_url = self.live_server_url + reverse('register')

    # Verify page link is now the one for Register
    self.assertEqual(current_url, register_url, 'Did not redirect to Register page')
