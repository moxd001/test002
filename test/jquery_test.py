from selenium import webdriver
import time
driver = webdriver.Chrome()
url="http://www.51wanj.com/admin/index.html?redirect=consumptionSta/consumptionSta.html&t=1557903767054"
driver.get(url)
# time.sleep(1)
# driver.maximize_window()
# hand=driver.window_handles
# print(len(hand))
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[3]/button[2]").click()
# driver.find_element_by_css_selector(".control-box>button:nth-child(2)").click() #这个方法不对
time.sleep(2)
# jq ="""
#         $('.control-box>button:nth-child(2)').click();
#         $('#username').val('test');
#         $('#password').val('657438');
#         $('.btn.btn-primary').click()
#
#     """
driver.execute_script("$('.control-box>button:nth-child(2)').click()")
driver.execute_script("$('#username').val('test')")
driver.execute_script("$('#password').val('657438')")
driver.execute_script("$('.btn.btn-primary').click()")
# driver.find_element_by_css_selector("[value='登录']").click()
time.sleep(10)
driver.quit()
