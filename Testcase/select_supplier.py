import unittest
from Business.select_supplier import Select_supplier

class Testcase(unittest.TestCase):
    def setUp(self):
        print("start------------>case")
    def tearDown(self):
        print("end-------------->case")

    def test_001(self):
        log5 = Select_supplier()
        log5.select_supplier("meng1","","")
        # 获取用于断言判断的登录后用户名
        data = log5.get_text("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span")
        # 进行断言判断
        self.assertEqual('meng1',data)


    def test_002(self):
        log5 = Select_supplier()
        log5.select_supplier("meng1","/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span[9]/em","/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span[27]/em")
        # 获取用于断言判断的登录后用户名
        data = log5.get_text("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span")
        # 进行断言判断
        self.assertEqual('meng1',data)


    def test_003(self):
        log5 = Select_supplier()
        log5.select_supplier("","/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span[9]/em","/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span[27]/em")
        # 获取用于断言判断的登录后用户名
        data = log5.get_text("xpath","/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span")
        # 进行断言判断
        self.assertEqual('meng1',data)




if __name__ == '__main__':
    unittest.main()