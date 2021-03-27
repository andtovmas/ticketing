import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Verify_Events(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print('Verify event filtering functionality by brand')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://dev.admin.theticketfairy.fluxtech.me/")

        # login profile page

        email = driver.find_element_by_id(
            'username').send_keys('john.doe@mailinator.com')
        passWord = driver.find_element_by_id('password').send_keys('123456')
        logBtn = driver.find_element_by_css_selector(
            ".login_btn[type='submit']").click()

        driver.implicitly_wait(5)

        # select brand

        brnd = driver.find_element_by_id(
            'labelFilterBrand').send_keys('Payment Methods', Keys.ENTER)
        driver.implicitly_wait(5)

        # Verify that there are 5 events displayed and all events are attached to the  (Brand name: Payment Methods)

        links = driver.find_elements_by_xpath(
            "//a[contains(.,'Payment Methods')]")

        print("The", len(links), " events are attached to the Payment Methods")

    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()
