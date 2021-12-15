import unittest
from Business.add_supplier import Add_supplier



class Testcase(unittest.TestCase):

    def setUp(self):
        print("start---------->case")

    def tearDown(self):
        print("end------------>case")


    # 供应商新增成功(全部输入内容)
    def test_001(self):
        log2 = Add_supplier()
        log2.add_supplier("meng1","河北","孟","13552325889","12","32","52")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log2.get_text("xpath","//div[@class='ivu-table-cell']/span[text()='meng1']")
        # 进行断言判断
        self.assertEqual('meng1',data)

    # 供应商新增成功(不输入营业执照号、税务登记号、备注)
    def test_002(self):
        log2 = Add_supplier()
        log2.add_supplier("meng1", "河北", "孟", "13552325889", "", "", "")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log2.get_text("xpath", "//div[@class='ivu-table-cell']/span[text()='meng1']")
        # 进行断言判断
        self.assertEqual('meng1', data)

    # 供应商新增不成功(不输入供应商名称)
    def test_003(self):
        log2 = Add_supplier()
        log2.add_supplier("", "河北", "孟", "13552325889", "", "", "")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log2.get_text("xpath", "//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入供货商名称']")
        # 进行断言判断
        self.assertEqual('请输入供货商名称', data)

    # 供应商新增不成功(不输入联系地址)
    def test_004(self):
        log2 = Add_supplier()
        log2.add_supplier("meng1", "", "孟", "13552325889", "", "", "")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log2.get_text("xpath", "//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入联系地址']")
        # 进行断言判断
        self.assertEqual('请输入联系地址', data)

    # 供应商新增不成功(不输入联系人)
    def test_005(self):
        log2 = Add_supplier()
        log2.add_supplier("meng1", "河北", "", "13552325889", "", "", "")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log2.get_text("xpath", "//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入联系人']")
        # 进行断言判断
        self.assertEqual('请输入联系人', data)

    # 供应商新增不成功(不输入联系方式)
    def test_006(self):
        log2 = Add_supplier()
        log2.add_supplier("meng1", "河北", "3", "", "", "", "")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log2.get_text("xpath", "//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请输入联系方式']")
        # 进行断言判断
        self.assertEqual('请输入联系方式', data)






if __name__ == '__main__':
    unittest.main()