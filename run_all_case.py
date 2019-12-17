import unittest
from common import HTMLTestRunner_cn
case_dir ="D:\\PyCharm 5.0.4\\python_test\\case\\"
discover = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test*.py",top_level_dir=None)
reportPath = "D:\\PyCharm 5.0.4\\python_test\\report\\"+"result.html"
fp =open(reportPath,"wb")
runner =HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                         title="登录测试用例",
                                         description="nn",
                                         retry=1)
runner.run(discover)
fp.close()