from common.base import Base
from selenium import webdriver


login_url="http://localhost:80/zentao/"
class Login(Base):
    loc_user=("id","account")
    loc_psd=("name","password")
    loc_sub=("id","submit")
    loc_keep=("id","keepLoginon")
    loc_forget=("link text","忘记密码")
    loc_user_name=("link text",'退出')
    loc_refresh=("link text","刷新")

    def input_user(self,text):
       res=self.sendKeys(self.loc_user,text)
       return res
    def input_psw(self,psw):
       res=self.sendKeys(self.loc_psd,psw)
       return res
    def login_button(self):
        self.click(self.loc_sub)
    def keep_login(self):
        self.click(self.loc_keep)
    def forget_password(self):
        self.click(self.loc_forget)
    def login(self,username="admin",password="123456",keep_login_button=False):
        self.sendKeys(self.loc_user,username)
        self.sendKeys(self.loc_psd,password)
        if keep_login_button:self.keep_login()
        self.click(self.loc_sub)
    def get_user_name(self):
        res=self.get_login_username(self.loc_user_name)
        return res
    def alert_accept(self):
        alert=self.is_alert()
        if alert:
            text=alert.text
            print(text)
            alert.accept()
    def refresh_exist(self):
        res=self.get_login_username(self.loc_refresh)
        return res

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get(login_url)
    log=Login(driver)
    log.login(keep_login_button=True)
    driver.quit()







    # login.input_user("admin")
    # login.input_psw("123456")
    # login.keep_login()
    # login.login_button()
    # r=login.get_user_name()
    # print(r)