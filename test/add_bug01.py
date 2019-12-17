import time
import unittest

from selenium import webdriver

from case.test_add_bug_class import AddBug


class BugCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("http://localhost:80/zentao/")
        cls.driver.maximize_window()
        cls.zentao=AddBug(cls.driver)
        cls.zentao.login("admin","123456")
    def test_addbug01(self):
        title="提bug"+time.strftime("%Y_%m_%d_%H_%M_%S")
        self.zentao.add_bug(title)
        res=self.zentao.is_add_bug_success(title)
        self.assertTrue(res)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()
