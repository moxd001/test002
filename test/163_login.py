from selenium import  webdriver
from time import sleep
url="https://mail.126.com/"
driver = webdriver.Chrome()
driver.get(url)
sleep(4)
frame = driver.find_elements_by_tag_name("iframe")[0]
driver.switch_to.frame(frame)
sleep(2)
driver.find_element_by_name("email").send_keys("qqqyug")
sleep(1)
driver.find_element_by_name("password").send_keys("da982864376")
driver.find_element_by_id("dologin").click()
sleep(2)
# print(driver.title)
if("网易邮箱" in driver.title):
    print("登录成功！！！")
else:
    print("登陆失败！！！")
sleep(5)
driver.quit()
