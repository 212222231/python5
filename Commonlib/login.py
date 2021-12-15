# coding:utf-8
from Commonlib.Commonlib import Commonshare
from time import sleep
from Commonlib.Log import Log


class Login(Commonshare):
    # log2 = Log()
    def login(self):
        # 在浏览器打开网址
        self.open_url("http://60.205.209.87/merchant-web/#/login")
        # 定位并输入用户名和密码
        self.input_date("css","input[placeholder='请输入用户名']","mengyao")
        self.input_date("css","input[placeholder='请输入密码']","123456")
        # 点击登录按钮
        self.click("css","button[type='button']")
        sleep(2)


if __name__ == '__main__':
    login = Login()