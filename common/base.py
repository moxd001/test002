from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self,locator):
        ele = WebDriverWait(self.driver,5,self.t).until(lambda x : x.find_element(*locator))
        return ele
    def sendKeys(self,locator,text,is_clear=False):
        ele = self.findElement(locator)
        if is_clear:
            ele.clear()
        ele.send_keys(text)
    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()
    def is_title(self,_title):
        try:
            res=WebDriverWait(self.driver,self.timeout,self.t).until(ec.title_is(_title))
            return res
        except:
            return False
    def is_title_contions(self,_title):
        try:
            res=WebDriverWait(self.driver,self.timeout,self.t).until(ec.title_contains(_title))
            return res
        except:
            return False
    def is_text_in_element(self,locator,_text):
        try:
            res=WebDriverWait(self.driver,self.timeout,self.t).until(ec.text_to_be_present_in_element(locator,_text))
            return res
        except:
            return False
    def is_alert(self):
        try:
            res=WebDriverWait(self.driver,self.timeout,self.t).until(ec.alert_is_present())
            return res
        except:
            return False
    def get_login_username(self,locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            return ""
    def move_to_element(self,loctor):
        ele=self.findElement(loctor)
        ActionChains(driver).move_to_element(ele).perform()
    def select_by_index(self,locator,index=0):
        ele=self.findElement(locator)
        Select(ele).select_by_index(index)
    def select_by_value(self,locator,value):
        ele=self.findElement(locator)
        Select(ele).select_by_value(value)
    def select_by_text(self,locator,text):
        ele=self.findElement(locator)
        Select(ele).select_by_visible_text(text)
    def js_scroll_end(self):
        js_heig="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_heig)
    def js_focus(self,locator):
        target=self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
    def js_scroll_top(self):
        js_heig="window.scrollTo(0,0)"
        self.driver.execute_script(js_heig)







if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://sz.ganji.com/")
    base = Base(driver)
    base.js_scroll_end()
    time.sleep(4)
    base.js_scroll_top()
    time.sleep(4)
    ele=("link text","新车")
    base.js_focus(ele)


















    # driver.get("http://www.weishopyun.com/admin/")
    # loc1 = (By.XPATH,"/html/body/div[5]/div[2]/div[3]/div[2]/button")
    # loc2 = (By.ID,"username")
    # loc3 = (By.ID,"password")
    # loc4 = (By.ID,"validCode")
    # loc5 = (By.CSS_SELECTOR,".btn.btn-primary")
    #
    # base = Base(driver)
    # base.click(loc1)
    # base.sendKeys(loc2,"admin")
    # base.sendKeys(loc3,"668866")
    # base.sendKeys(loc4,"123")
    # base.click(loc5)
    driver.quit()
