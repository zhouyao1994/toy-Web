#coding:utf8
#create by zhouyao
#data: 16-12-27

from __future__ import unicode_literals
import unittest
from app import create_app,db


class Test_db(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def xxx_test_can_accesss(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    unittest.main()