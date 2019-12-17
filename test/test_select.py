from selenium import webdriver
from selenium.webdriver.support.select import Select #导入Select 类
from selenium.webdriver.common.action_chains import ActionChains #鼠标操作
import time
driver = webdriver.Chrome()
url="https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
time.sleep(1)
#第一种定位下拉框的方法(万能的)
# s= driver.find_element_by_id("nr")
# driver.find_element_by_xpath("//*[@id='nr']/option[2]").click()
# time.sleep(2)

# 通过Select类去定位
s = driver.find_element_by_id("nr")
Select(s).select_by_value("20") #通过value值去定位
time.sleep(2)
# s.click()
# time.sleep(1)
# Select(s).select_by_index(0) #通过索引去定位
# s.click()
# time.sleep(1)
# Select(s).select_by_visible_text("每页显示50条")
# s.click()
# time.sleep(5)
driver.find_element_by_link_text("保存设置").click()
time.sleep(1)
a = driver.switch_to.alert
time.sleep(2)
print(a.text) #打印弹窗内容
#  a.accept()  #确定
# a.dismiss() #取消
time.sleep(5)
driver.quit()