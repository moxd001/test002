from selenium import webdriver

from common.base import Base

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
loc1=("link text","新闻")
zen=Base(driver)
s1=zen.is_title("百度一下，你就知道")
print(s1)
s2=zen.is_title_contions("百度")
print(s2)
s3=zen.is_text_in_element(loc1,"新闻")
print(s3)
s4=zen.findElement(loc1).text
print(s4)
driver.quit()



