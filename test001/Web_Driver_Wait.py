from selenium import webdriver #导入webdriver包
from selenium.webdriver.support.wait import WebDriverWait #导入WebDriverWait包， wait或者ui都可以
# from selenium.webdriver.common.by import By
driver = webdriver.Chrome()#打开谷歌浏览器
# driver.maximize_window()# 窗口最大化
driver.get('http://www.weishopyun.com/admin/') #访问地址
def findElement(driver,locator,timeout=10,t=0.5):
    ele=WebDriverWait(driver,timeout,t).until(lambda x:x.find_element(*locator))
    return ele
#需要引用By包
# loc1=(By.XPATH,"/html/body/div[5]/div[2]/div[3]/div[2]/button")
# loc2=(By.ID,"username")
# loc3=(By.ID,"password")
# loc4=(By.ID,"validCode")
# loc5=(By.XPATH,".//*[@value='登录']")

#不需要引用By包
loc1=("xpath","/html/body/div[5]/div[2]/div[3]/div[2]/button")
loc2=("id","username")
loc3=("id","password")
loc4=("id","validCode")
loc5=("xpath",".//*[@value='登录']")


findElement(driver,loc1).click()
findElement(driver,loc2).send_keys("admin")
findElement(driver,loc3).send_keys("668866")
findElement(driver,loc4).send_keys("123456")
findElement(driver,loc5).click()









# ele1=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[2]/button"))
# 调用显示等待WebDriverWait,timeout = 5,poll_frequency = 0.5,ignore_exception = None
'''
from selenium.webdriver.support.ui import WebDriverWait \n
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''
# WebDriverWait(self,driver,timeout,poll_frequency=POLL_FREQUENCY,ignore_expcetions=None)
# driver： 打开浏览器的一个实例参数
# timeout： 超时总时长
# poll_frequency：循环查询间隔时间 默认为0.5秒
# ignore_exception:忽略异常，默认忽略NoSuchElementException
# ele1.click()
# ele2=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_id("username")).send_keys("admin")
# ele3=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_id("password")).send_keys("668866")
# ele4=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_id("validCode")).send_keys("123456")
# ele5=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_xpath(".//*[@value='登录']")).click()
driver.quit()