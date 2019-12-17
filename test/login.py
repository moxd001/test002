#coding:utf-8
from selenium import webdriver
import time
# 火狐加载配置文件
# profile_directory = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wpzcutvb.default"
# profile =webdriver.FirefoxProfile(profile_directory)
# driver =webdriver.Firefox(profile)

# 谷歌加载配置文件
option =webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://www.aizj168.com/admin/index.html?redirect=undefined&t=1555493258257")
time.sleep(4)
driver.quit()
