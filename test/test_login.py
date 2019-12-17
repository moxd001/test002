import unittest

from selenium import webdriver

from common.base import Base


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.weishopyun.com/admin/')
        self.jc=Base(self.driver)
    def test_login(self):
        loc1=("xpath","/html/body/div[5]/div[2]/div[3]/div[2]/button")
        loc2=("id","username")
        loc3=("id","password")
        loc4=("id","validCode")
        loc5=("xpath",".//*[@value='登录']")
        loc6=("id","userName")

        self.jc.click(loc1)
        self.jc.sendKeys(loc2,"adm")
        self.jc.sendKeys(loc2,"admin",True)
        self.jc.sendKeys(loc3,"668866")
        self.jc.sendKeys(loc4,"123456")
        self.jc.click(loc5)
        t=self.jc.findElement(loc6).text
        self.assertEqual("admin",t)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()