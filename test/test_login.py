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
        brower.get("http://localhost:5000/login")
        # 登录框
        user_anme_element = brower.find_element_by_id("username")
        pass_element = brower.find_element_by_id("password")
        sub = brower.find_element_by_id("submit")

        #输入用户名，密码
        user_anme_element.send_keys("demo")
        pass_element.send_keys("demo")

        #登录
        sub = sub.click()
        # time.sleep(2)

        brower.get("http://localhost:5000/register")
        time.sleep(2)
        ruser = brower.find_element_by_id("username")
        rpass = brower.find_element_by_id("password")
        rpass2 = brower.find_element_by_id("password2")
        rsub = brower.find_element_by_id("submit")

        ruser.send_keys("demo3")
        rpass.send_keys("demo1")
        rpass2.send_keys("demo1")
        rsub.click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()