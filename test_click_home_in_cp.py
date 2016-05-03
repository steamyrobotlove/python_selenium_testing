import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CpComClickHome(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_click_home_in_cp(self):
        driver = self.driver
        driver.get("http://www.californiapsychics.com")
        elem = driver.find_element_by_link_text("HOME")
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
        
