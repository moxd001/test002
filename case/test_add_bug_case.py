from selenium import webdriver
import unittest
from pages.login_pages import Login
from pages.add_bug_pages import AddBug
import time
url="http://localhost:80/zentao/"
class AddBugCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(url)
        log=Login(cls.driver)
        log.login()
        cls.bug=AddBug(cls.driver)



    def test001(self):
        tittle="添加bug"+time.strftime("%Y_%m_%d_%H_%M_%S")
        self.bug.add_bug(tittle)
        r=self.bug.is_add_bug_success(tittle)
        self.assertTrue(r)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()