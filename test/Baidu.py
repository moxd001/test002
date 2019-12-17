from selenium import webdriver
import unittest
import time
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
    def test_001(self):
        self.driver.find_element_by_id("kw").send_keys("nba")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        t = self.driver.title
        print(t)
        self.assertEqual("nba_百度搜索",t)
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()