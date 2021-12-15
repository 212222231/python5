from Commonlib.Commonlib import Commonshare
from time import sleep

class Add_supplier(Commonshare):
    def add_supplier(self,name,address,contact,phone,license,registration,remarks):
        # 在浏览器打开网址
        self.open_url("http://60.205.209.87/merchant-web/#/login")
        # # 定位并输入用户名和密码
        self.input_date("css", "input[placeholder='请输入用户名']", "mengyao")
        self.input_date("css", "input[placeholder='请输入密码']", "123456")
        # 点击登录按钮
        self.click("css", "button[type='button']")
        sleep(3)
        # 点击新增按钮
        self.click("xpath","//div[@class='addSupplier']/i[@class='iconfont icon-xinzeng']")
        self.input_date("css","input[placeholder='请输入供货商名称(必填)']",name)
        self.input_date("css","input[placeholder='请输入联系地址(必填)']",address)
        self.input_date("css","input[placeholder='请输入联系人(必填)']",contact)
        self.input_date("css","input[placeholder='请输入联系方式(必填)']",phone)
        self.input_date("css","input[placeholder='请输入营业执照号']",license)
        self.input_date("css", "input[placeholder='请输入税务登记号']", registration)
        sleep(2)
        self.input_date("css", "input[placeholder='请输入备注']", remarks)
        self.click("xpath","//div[@class='handle']/i[@class='iconfont icon-tijiao']")
        sleep(1)
        self.sav_screenshot(img_name='add_supplier_')

if __name__ == '__main__':
    log2 = Add_supplier()






