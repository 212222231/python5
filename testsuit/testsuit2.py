import unittest
# 导入生成html格式测试报告的库
from Commonlib.HTMLTestRunner import HTMLTestRunner
# from Testcase import login
from Testcase import login,add_Warehouse,add_supplier,add_drugs


# 创建测试套件
mysuit = unittest.TestSuite()
mysuit.addTest(unittest.makeSuite(login.Testcase))
mysuit.addTest(unittest.makeSuite(add_supplier.Testcase))
mysuit.addTest(unittest.makeSuite(add_Warehouse.Testcase))
mysuit.addTest(unittest.makeSuite(add_drugs.Testcase))

# 生成html格式测试报告的步骤
with open('../baogao/report11.27.html','wb')as f:
        HTMLTestRunner(
            stream=f,
            title='进销存系统报告',
            description='登录、新建供货商、仓库模块',
             verbosity=2
        ).run(mysuit)

if __name__ == '__main__':
    unittest.main()