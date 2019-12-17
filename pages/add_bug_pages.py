from selenium import webdriver
from common.base import Base
from pages.login_pages import Login

class AddBug(Base):#继承Base
    loc_test=("link text","测试")
    loc_bug=("link text","Bug")
    loc_tj_bug=("xpath","//*[@id='createActionMenu']/a")
    loc_trunk=("xpath","//*[@id='openedBuild_chosen']/ul")
    loc_trunk_choose=("xpath",'//*[@id="openedBuild_chosen"]/div/ul/li')
    loc_title=("id","title")
    # 需要切换iframe
    loc_body=("class name","article-content")
    loc_submit=("id","submit")
    loc_frame=("class name","ke-edit-iframe")
    loc_new=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def add_bug(self,title="添加bug"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_tj_bug)
        self.click(self.loc_trunk)
        self.click(self.loc_trunk_choose)
        self.sendKeys(self.loc_title,title)
        frame=self.findElement(self.loc_frame)
        self.driver.switch_to.frame(frame)
        self.sendKeys(self.loc_body,"ssss")
        self.driver.switch_to.parent_frame()
        self.click(self.loc_submit)
    def is_add_bug_success(self,bug_title):
        res=self.is_text_in_element(self.loc_new,bug_title)
        return res

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://localhost:80/zentao/")
    add=AddBug(driver)
    l=Login(driver)
    l.login()
    add.add_bug()
