import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ZendeskSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
	self.driver.implicitly_wait(30)

    def test_search_in_zendesk(self):
        driver = self.driver
        driver.get("https://www.zendesk.com/")
        self.assertIn("Zendesk | Customer Service Software & Support Ticket System", driver.title)
        self.driver.find_element_by_name("search").clear()
	self.driver.find_element_by_name("search").send_keys(" ")
        self.driver.find_element_by_name("search").send_keys(Keys.RETURN)
        assert "0 results." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
