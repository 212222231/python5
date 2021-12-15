from Commonlib.Commonlib import Commonshare
from time import sleep

class Add_drugs(Commonshare):
    def add_drugs(self,name,type,mold,company,warehouse,number,warning,saturation):
    # def add_drugs(self, name, company,  number, warning, saturation):
        # 在浏览器打开网址
        self.open_url("http://60.205.209.87/merchant-web/#/login")
        # 定位并输入用户名和密码
        self.input_date("css", "input[placeholder='请输入用户名']", "mengyao")
        self.input_date("css", "input[placeholder='请输入密码']", "123456")
        # 点击登录按钮
        self.click("css", "button[type='button']")
        # 点击药品模块
        self.click("xpath","/html/body/div/div/div[1]/div[1]/ul/li[2]/div")
        self.click("xpath","/html/body/div/div/div[1]/div[1]/ul/li[2]/ul/a[1]")
        # 点击新增按钮
        self.click("xpath","//div[@class='tableHandle']/span[text()='新增']")
        # 新增药品
        self.input_date("css","input[placeholder='请输入药品名称(必填)']",name)
        self.click("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/i")
        sleep(2)
        # self.click("xpath",f"//ul[@class='ivu-select-dropdown-list']/li[text()={type}]")
        # self.click("xpath", "//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']")
        self.click("xpath", type)
        sleep(1)
        self.click("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/i")
        # self.click("xpath",f"//ul[@class='ivu-select-dropdown-list']/li[text()={mold}]")
        # self.click("xpath", "//ul[@class='ivu-select-dropdown-list']/li[text()='优选']")
        self.click("xpath", mold)
        self.input_date("css", "input[placeholder='请输入单位(必填)']", company)
        sleep(1)
        self.click("xpath", "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[5]/div[2]/div[1]/div/i")
        # self.click("xpath",f"//ul[@class='ivu-select-dropdown-list']/li[text()={warehouse}]")
        # self.click("xpath","//ul[@class='ivu-select-dropdown-list']/li[text()='meng2']")
        self.click("xpath", warehouse)
        self.input_date("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[6]/div[2]/input",number)
        self.input_date("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[7]/div[2]/div[2]/input",warning)
        self.input_date("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[8]/div[2]/div[2]/input",saturation)
        sleep(2)
        # 提交
        self.click("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[1]/button/span/span")
        sleep(2)
        self.sav_screenshot(img_name='add_drugs_')


    if __name__ == '__main__':
        log3 = Add_drugs()


