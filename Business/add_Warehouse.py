from Commonlib.Commonlib import Commonshare
from time import sleep

class Add_Warehouse(Commonshare):
    def add_Warehouse(self,name,remarks):
        # 在浏览器打开网址
        self.open_url("http://60.205.209.87/merchant-web/#/login")
        # 定位并输入用户名和密码
        self.input_date("css", "input[placeholder='请输入用户名']", "mengyao")
        self.input_date("css", "input[placeholder='请输入密码']", "123456")
        # 点击登录按钮
        self.click("css", "button[type='button']")
        sleep(2)
        # 点击仓库管理按钮
        self.click("xpath","/html/body/div/div/div[1]/div[1]/ul/li[1]/ul/a[2]")
        # 点击新增仓库
        self.click("xpath","//div[@class='handle']/span[text()=' 新增仓库 ']")
        # 输入信息
        self.input_date("css","input[placeholder='请输入仓库名称(必填)']",name)
        self.input_date("css","input[placeholder='请输入备注']",remarks)
        # 提交
        self.click("css","html body div#app div.layout div.right.ivu-layout div.content.ivu-layout-content div.newStoreHouse div.title button.handle.ivu-btn.ivu-btn-text span i.iconfont.icon-tijiao")
        sleep(1)
        self.sav_screenshot(img_name='add_warehouse_')

if __name__ == '__main__':
    log3 = Add_Warehouse()