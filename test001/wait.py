from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
'''
Example:
        from selenium.webdriver.support.ui import WebDriverWait \n
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
        is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                    until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''
driver =webdriver.Chrome()
driver.get("http://www.weishopyun.com/admin/index.html?t=1573786954229")
# ele = WebDriverWait(driver,10).until(lambda x : x.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[2]/button"))
# ele.click()
# element1 = WebDriverWait(driver,10).until(lambda x : x.find_element_by_id("username"))
# element1.send_keys("admin")
# element2 = WebDriverWait(driver,10).until(lambda x : x.find_element_by_id("password"))
# element2.send_keys("668866")
# element3 = WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("validCode"))
# element3.send_keys("123")
# element4 = WebDriverWait(driver,10).until(lambda x : x.find_element_by_css_selector(".btn.btn-primary"))
# element4.click()http://qian.miaodkd.com/admin
# driver.quit()

def findElement(driver,locator,timeout=10,t=0.5):
    ele = WebDriverWait(driver,timeout,t).until(lambda x : x.find_element(*locator))
    return ele

loc1 = ("xpath","/html/body/div[5]/div[2]/div[3]/div[2]/button")
loc2 = ("id","username")
loc3 = ("id","password")
loc4 = ("id","validCode")
loc5 = ("css selector",".btn.btn-primary")

findElement(driver,loc1).click()
findElement(driver,loc2).send_keys("admin")
findElement(driver,loc3).send_keys("668866")
findElement(driver,loc4).send_keys("123")
findElement(driver,loc5).click()
driver.quit()