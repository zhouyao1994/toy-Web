#coding:utf8
#create by zhouyao
#data: 16-12-27

from __future__ import unicode_literals
from selenium import webdriver
import time
import unittest


class NewvistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_accesss(self):
        brower = self.browser
        #查看能够运行
        brower.get("http://127.0.0.1:5000/hello")
        # time.sleep(3)
        #是否有helloword
        self.assertIn("Hello",brower.find_element_by_xpath("//body").text)

    def test_login(self):
        brower = self.browser
        brower.get("http://127.0.0.1:5000/login")
        time.sleep(3)
        self.assertIn("邮箱",brower.find_element_by_xpath(""))

if __name__ == '__main__':
    unittest.main()