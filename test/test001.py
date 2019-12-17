# coding:utf-8
from selenium import webdriver
import time
# profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wpzcutvb.default"
# profile_directory = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default"
driver = webdriver.Chrome()
driver.get("http://www.aizj168.com/admin/index.html?redirect=undefined&t=1555493258257")
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[2]/button").click()
time.sleep(3)
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("668866")
driver.find_element_by_id("validCode").send_keys("123456")
# driver.find_element_by_xpath("/html/body/form/article/div/div[4]/input").click()
driver.find_element_by_css_selector(".btn.btn-primary").click()
time.sleep(5)
driver.quit()
