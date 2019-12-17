from selenium import webdriver
import unittest
from pages.login_pages import Login,login_url
import ddt
from common.read_excel import ExcelUtil
import os
'''
1.输入正确的账号，正确的密码 并点击登录
2.输入账号，密码为空，并点击登录
3.错误的账号，密码，点击登录
'''
# testdata=({"user":"admin","psw":"123456","expect":"退出"},
#       {"user":"admin","psw":"1234567","expect":""},
#       {"user":"admin1","psw":"123456","expect":""},)
'''获取上一层路径：os.path.dirname
   获取当前层路径：os.path.realpath(__file__)
'''
propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
'''拼接路径：os.path.join'''
filepath=os.path.join(propath,"common","testdata.xlsx")
print(filepath)
data=ExcelUtil(filepath)
testdata=data.dict_data()
print (testdata)
@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(login_url)
        cls.log=Login(cls.driver)
    def setUp(self):
        self.log.alert_accept()
        self.driver.delete_all_cookies()
        self.driver.refresh()
    '''输入正确的账号，正确的密码 并点击登录'''
    @ddt.data(*testdata)
    def test001(self,testdata):
        print("--------开始测试---------")
        print("测试数据：%s"%testdata)
        self.login_case(testdata["user"],testdata["psw"],testdata["expect"])
        print("-------结束测试----------")


    def login_case(self,user,psd,expect):
        self.log.input_user(user)
        self.log.input_psw(psd)
        self.log.login_button()
        r=self.log.get_user_name()
        self.assertEqual(r,expect)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()



