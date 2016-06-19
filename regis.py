import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.zendesk.com/"
   
    
    def test_Register(self):
        driver = self.driver
        driver.get("https://www.zendesk.com/register/#getstarted")
        try: self.assertTrue(self.is_element_present(By.ID, "owner[email]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "owner[password]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Next"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Next").click()
    
 
    
    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()

