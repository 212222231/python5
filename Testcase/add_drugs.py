import unittest
from Business.add_drugs import Add_drugs

class Testcase(unittest.TestCase):

    def setUp(self):
        print("start---------->case")

    def tearDown(self):
        print("end------------>case")


    # 药品新增成功(全部输入内容)
    def test_001(self):
        log3 = Add_drugs()
        log3.add_drugs("孟瑶11","//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']","//ul[@class='ivu-select-dropdown-list']/li[text()='优选']","g","//ul[@class='ivu-select-dropdown-list']/li[text()='meng2']","32","52",'100')
        # log3.add_drugs("孟瑶6", "g", "32", "52", '100')
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-table-cell']/span[text()='孟瑶11']")
        # 进行断言判断
        self.assertEqual('孟瑶11',data)

    # 新增名称、剂型、剂量相同的药品（不能通过）
    def test_002(self):
        log3 = Add_drugs()
        # log3.add_drugs("孟瑶","饮片","优选","g","meng2","32","52",'100')
        log3.add_drugs("孟瑶8","//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']","//ul[@class='ivu-select-dropdown-list']/li[text()='优选']","g","//ul[@class='ivu-select-dropdown-list']/li[text()='meng2']","32","52",'100')
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='当前商品已存在']")
        # 进行断言判断
        self.assertEqual('当前商品已存在',data)


    # 药品新增失败(不输入药品名称)
    def test_003(self):
        log3 = Add_drugs()
        log3.add_drugs("","//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']","//ul[@class='ivu-select-dropdown-list']/li[text()='优选']","g","//ul[@class='ivu-select-dropdown-list']/li[text()='meng2']","32","52",'100')
        # log3.add_drugs("孟瑶6", "g", "32", "52", '100')
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入药品名称']")
        # 进行断言判断
        self.assertEqual('请输入药品名称', data)

    # 药品新增失败(不输入药品单位)
    def test_004(self):
        log3 = Add_drugs()
        log3.add_drugs("孟瑶9","//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']","//ul[@class='ivu-select-dropdown-list']/li[text()='优选']","","//ul[@class='ivu-select-dropdown-list']/li[text()='meng2']","32","52",'100')
        # log3.add_drugs("孟瑶6", "g", "32", "52", '100')
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入药品单位']")
        # 进行断言判断
        self.assertEqual('请输入药品单位', data)

    # 药品新增失败(不选择药品仓库)
    def test_005(self):
        log3 = Add_drugs()
        log3.add_drugs("孟瑶9","//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']","//ul[@class='ivu-select-dropdown-list']/li[text()='优选']","g","","32","52",'100')
        # log3.add_drugs("孟瑶6", "g", "32", "52", '100')
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请选择存放仓库']")
        # 进行断言判断
        self.assertEqual('请选择存放仓库', data)

    # 药品新增成功(不输入库存编号、库存预警、库存饱和)
    def test_006(self):
        log3 = Add_drugs()
        log3.add_drugs("孟瑶12","//ul[@class='ivu-select-dropdown-list']/li[text()='饮片']","//ul[@class='ivu-select-dropdown-list']/li[text()='优选']","g","//ul[@class='ivu-select-dropdown-list']/li[text()='meng2']","32","52",'100')
        # log3.add_drugs("孟瑶6", "g", "32", "52", '100')
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath", "//div[@class='ivu-table-cell']/span[text()='孟瑶12']")
        # 进行断言判断
        self.assertEqual('孟瑶12', data)

if __name__ == '__main__':
    unittest.main()