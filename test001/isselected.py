import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #鼠标操作
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #导入Select 类

from common.base import Base

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.maximize_window()
base = Base(driver)
loc1=("link text" ,"设置")
loc2=("link text" ,"搜索设置")
loc3=(By.ID,"nr")
loc4=(By.LINK_TEXT,"保存设置")
mouse =base.findElement(loc1)
ActionChains(driver).move_to_element(mouse).perform()
base.findElement(loc2).click()
s=base.findElement(loc3)
Select(s).select_by_value("20")
base.click(loc4)
a = driver.switch_to.alert
print(a.text)
a.accept()
time.sleep(5)
driver.quit()

