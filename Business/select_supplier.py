from Commonlib.Commonlib import Commonshare
from time import sleep

class Select_supplier(Commonshare):
    def select_supplier(self,name,one,last):
        # 在浏览器打开网址
        self.open_url("http://60.205.209.87/merchant-web/#/login")
        # 定位并输入用户名和密码
        self.input_date("css", "input[placeholder='请输入用户名']", "mengyao")
        self.input_date("css", "input[placeholder='请输入密码']", "123456")
        # 点击登录按钮
        self.click("css", "button[type='button']")
        # 点击供应商名称栏
        self.input_date("css","input[placeholder='请输入供货商名称']",name)
        if one!='':
            self.click("css","input[placeholder='请选择日期范围']")
            self.click("xpath",one)
            self.click("xpath",last)
            self.click("xpath", "//div[@class='handleItem']/span[text()='搜索']")
            self.sav_screenshot(img_name='select_supplier_')
        else:
            self.click("xpath", "//div[@class='handleItem']/span[text()='搜索']")
            self.sav_screenshot(img_name='select_supplier_')
        # self.click("xpath","/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span[9]/em")
        # self.click("xpath", "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span[27]/em")
        # self.click("xpath","//div[@class='handleItem']/span[text()='搜索']")
        # self.sav_screenshot(img_name='select_supplier_')


if __name__ == '__main__':
    log5 = Select_supplier()