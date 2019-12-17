import time
class LoginTest():

    def __init__(self,driver):
        self.driver = driver


    def login(self,name,psw,code):
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("password").send_keys(psw)
        self.driver.find_element_by_id("validCode").send_keys(code)
        time.sleep(2)
        self.driver.find_element_by_css_selector(".btn.btn-primary").click()
    def get_login_username(self,username="userName"):
        try:
            t = self.driver.find_element_by_id(username).text
            return t
        except:
            return ""
    def click_button(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[2]/button").click()
