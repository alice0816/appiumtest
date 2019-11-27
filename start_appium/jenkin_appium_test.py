import unittest
import os
from selenium import webdriver
import HTMLTestRunner
 5
 6 class apptest(unittest.TestCase):
 7     def setUp(self):
 8         PATH = lambda p: os.path.abspath(
 9             os.path.join(os.path.dirname(__file__), p))
11         desired_caps = {}
12         desired_caps['deviceName'] = 'VBJ4C18607003439'  # adb devices查到的设备名
13         desired_caps['platformName'] = 'Android'
14         desired_caps['platformVersion'] = '8.1.0'  # android 系统版本
15         desired_caps['appPackage'] = 'com.aerozhonghuan.serialporttool'  # 被测App的包名
16         desired_caps['appActivity'] = 'com.aerozhonghuan.serialporttool.MainActivity'  # 启动时的Activity
17         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
18     def testApp(self):
19         driver = self.driver
20         el = driver.find_element_by_id("com.aerozhonghuan.serialporttool:id/btn_heartbeat")
21         el.click()
22         print('第一个appium脚本运行成功了')
23         filename = r'E:\aaaaaa\report.html' #E:\aaaaaa\report.html 这个目录下生成测试报告
24         fp = open(filename, 'wb+')
25         runner = HTMLTestRunner.HTMLTestRunner(
26             stream=fp,
27             title=u'APP自动化测试'
28         )
29         runner.run(self.suite())
30         fp.close()
31     def suite(self):
32         suite = unittest.TestSuite()
33         suite.addTest(apptest("testApp"))
34         return suite
35
36     def tearDown(self):
37         driver = self.driver
38         driver.quit()
39 if __name__ == '__main__':
40     unittest.main()