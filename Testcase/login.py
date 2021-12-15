import unittest
from Business.login import Login
import time
# import sys
# sys.path.append('D:\my\进销存python\Business\login.py')

class Testcase(unittest.TestCase):
    def setUp(self):
        print("start---------->case")

    def tearDown(self):
        print("end------------>case")

    # 登录成功
    '''登录成功'''
    def test_001(self):
        log = Login()
        log.login("mengyao","12345")
        # 获取用于断言判断的登录后用户名
        data = log.get_text("xpath","//div[@class='handleItem name']/span[text()='孟瑶']")
        # 进行断言判断
        self.assertEqual('孟瑶',data)

    @unittest.skip("don't run this case!")
    # 什么都不输入
    def test_002(self):
        log = Login()
        log.login("","")
        # 获取用于断言弹窗的提示文案路径
        data = log.get_text("xpath","//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入用户名']")
        # 进行断言判断
        self.assertEqual('请输入用户名',data)

    # 输入账号，不输入密码
    def test_003(self):
        log = Login()
        log.login("mengyao", "")
        # 获取用于断言弹窗的提示文案路径
        data = log.get_text("xpath", "//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入密码']")
        # 进行断言判断
        self.assertEqual('请输入密码', data)



    # 不输入账号，只输入密码
    def test_004(self):
        log = Login()
        log.login("", "111111")
        # 获取用于断言弹窗的提示文案路径
        data = log.get_text("xpath","//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入用户名']")
        # 进行断言判断
        self.assertEqual('请输入用户名', data)



if __name__ == '__main__':
    unittest.main()