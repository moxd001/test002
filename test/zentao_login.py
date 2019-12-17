import unittest

from selenium import webdriver

from common import base


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("http://localhost:80/zentao")
        cls.zentao= base.Base(cls.driver)
    def setUp(self):
       pass
    def tearDown(self):
        loc1=("link text","退出")
        try:
            self.zentao.click(loc1)
            self.driver.refresh()
        except:
            pass
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        loc1=("id","account")
        loc2=("name","password")
        loc3=("id","submit")
        loc4=("link text","退出")

        self.zentao.sendKeys(loc1,"admin")
        self.zentao.sendKeys(loc2,"123456")
        self.zentao.click(loc3)
        t=self.zentao.is_text_in_element(loc4,'退出')
        assert t
        print(t)
    def test_002(self):
        loc1=("id","account")
        loc2=("name","password")
        loc3=("id","submit")
        loc4=("link text","退出")

        self.zentao.sendKeys(loc1,"admin1")
        self.zentao.sendKeys(loc2,"123456")
        self.zentao.click(loc3)
        t=self.zentao.is_text_in_element(loc4,'退出')
        assert t
        print(t)

if __name__=="__main__":
    unittest.main()