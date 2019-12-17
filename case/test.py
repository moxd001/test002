import time
import unittest
from selenium import webdriver
from test001.LoginTest1 import LoginTest

class Login(unittest.TestCase):
    '''登录测试类'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.weishopyun.com/admin/")
        cls.logintest=LoginTest(cls.driver)
    def setUp(self):
        time.sleep(2)
        self.logintest.click_button()
        # self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[2]/button").click()
    def tearDown(self):
        self.driver.delete_all_cookies() #清除cookies
        self.driver.refresh() # 刷新
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # 登录函数
    # def login(self,name,psw,code):
    #     self.driver.find_element_by_id("username").send_keys(name)
    #     self.driver.find_element_by_id("password").send_keys(psw)
    #     self.driver.find_element_by_id("validCode").send_keys(code)
    #     time.sleep(2)
    #     self.driver.find_element_by_css_selector(".btn.btn-primary").click()
    def test_001(self):
        '''登录成功的测试用例 用户名为：admin 密码为:668866'''
        self.logintest.login("admin","668866","123456")
        time.sleep(2)
        t=self.logintest.get_login_username()
        # t = self.driver.find_element_by_id("userName").text
        # print(t)
        self.assertEqual("admin",t)
    def test_002(self):
        '''登录失败的测试用例 用户名为：admin 密码为:123456'''
        self.logintest.login("admin","123456","123456")
        time.sleep(2)
        t1=self.logintest.get_login_username()
        # t1 = self.driver.find_element_by_css_selector(".g-alert").text
        # print(t1)
        self.assertIn("",t1)
if __name__ == "__main__":
    unittest.main()
