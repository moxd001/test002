from selenium import webdriver
driver = webdriver.Chrome()
while True:
    driver.get("http://www.xinkuainet.com.cn/reg.aspx?no=38900N")
    driver.delete_all_cookies()
    driver.refresh()
    # driver.quit()