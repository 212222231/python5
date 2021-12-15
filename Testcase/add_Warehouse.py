import unittest
from Business.add_Warehouse import Add_Warehouse

class Testcase(unittest.TestCase):
    def setUp(self):
        print("start---------->case")

    def tearDown(self):
        print("end------------>case")


    # 仓库创建成功(全部输入内容)
    def test_001(self):
        log3 = Add_Warehouse()
        log3.add_Warehouse("meng2","河北")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-table-cell']/span[text()='meng2']")
        # 进行断言判断
        self.assertEqual('meng2',data)

    # 仓库创建成功(不输入备注)
    def test_002(self):
        log3 = Add_Warehouse()
        log3.add_Warehouse("meng2","")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath","//div[@class='ivu-table-cell']/span[text()='meng2']")
        # 进行断言判断
        self.assertEqual('meng2',data)


    # 仓库创建不成功(不输入名称)
    def test_003(self):
        log3 = Add_Warehouse()
        log3.add_Warehouse("","")
        # 获取用于断言判断的新增成功后的供货商名称
        data = log3.get_text("xpath", "//div[@class='ivu-message-custom-content ivu-message-warning']/span[text()='请先输入仓库名称']")
        # 进行断言判断
        self.assertEqual('请先输入仓库名称',data)

if __name__ == '__main__':
    unittest.main()
