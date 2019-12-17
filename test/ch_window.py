from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "http://bj.ganji.com/"
driver.get(url)
driver.maximize_window()  #窗口最大化
driver.implicitly_wait(10)  #隐式等待 10秒最大等待时间 元素定位时候有作用
handle = driver.current_window_handle # 获取第一个窗口的句柄
driver.find_element_by_link_text("租房").click()
handles = driver.window_handles # 获取所有窗口的句柄
driver.switch_to.window(handles[1]) #切换到第二个窗口
print(driver.title)
driver.switch_to.window(handles[0])
print(driver.title)
driver.switch_to.window(handles[1])
driver.find_element_by_link_text("品牌公寓馆").click()
driver.switch_to.window(driver.window_handles[2])
print(driver.title)
driver.close()
print(handles)
driver.quit()