from selenium import webdriver
import unittest
from pages.login_pages import Login,login_url
'''
1.输入正确的账号，正确的密码 并点击登录
2.输入账号，密码为空，并点击登录
3.忘记密码
4.保持登录
'''
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(login_url)
        cls.log=Login(cls.driver)
    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
    '''输入正确的账号，正确的密码 并点击登录'''
    def test001(self):
        self.log.input_user("admin")
        self.log.input_psw("123456")
        self.log.login_button()
        r=self.log.get_user_name()
        self.assertEqual(r,"退出")
    '''输入账号，密码为空，并点击登录'''
    def test002(self):
        self.log.input_user("admin")
        self.log.login_button()
        self.log.alert_accept()
        r=self.log.get_user_name()
        self.assertEqual(r,"")

        '''保持登录'''
    def test003(self):
        self.log.input_user("admin")
        self.log.input_psw("123456")
        self.log.keep_login()
        self.log.login_button()
        r=self.log.get_user_name()
        self.assertEqual(r,"退出")
        '''忘记密码'''
    def test004(self):
        self.log.forget_password()
        r=self.log.refresh_exist()
        self.assertEqual(r,"刷新")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()



