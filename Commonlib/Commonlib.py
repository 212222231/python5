from selenium import webdriver
import time
import os
import logging
from datetime import datetime
from Commonlib.Log import Log


class Commonshare(object):
    def __init__(self):
        # 创建浏览器
        self.driver = webdriver.Firefox()
        # 隐式等待
        self.driver.implicitly_wait(3)
        # 浏览器最大化
        # self.driver.maximize_window()


    def open_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)


    def locateElement(self,locate_type,value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'tag':
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)

        # 返回定位元素
        if el is not None:
            return el


    # 对点击元素的封装
    def click(self,locate_type,value):
        # 调用locateElement
        el = self.locateElement(locate_type,value)
        # 执行点击操作
        el.click()

    # 直接对定位到的元素进行文本输入
    def input_date(self,locate_type,value,data):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 执行输入操作
        el.send_keys(data)

    # 获取定位到的元素中的文本内容<a>xxx</a>
    def get_text(self,locate_type,value):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.text


    # 获取定位到的元素中的标签属性
    def get_attr(self,locate_type,value,data):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.get_attribute(data)

    # 对截图进行封装
    def sav_screenshot(self,img_name):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 截图保存的文件名格式
        pic_path = "..//jietu//" + img_name + now + '_screen.png'  # 截图保存的路径
        # pic_path = "D:\my\进销存python\baogao\picture" + now + '_screen.png'
        # print(pic_path)
        self.driver.save_screenshot(pic_path)  # 调用Driver的截图保存功能

    # def log(self):
    #     logging.debug("a")
    #     logging.info("b")
    #     logging.basicConfig(filename="a.log")






    # 结束的时候清理了
    def __del__(self):
        time.sleep(3)
        self.driver.quit()

# if __name__ == '__main__':
#     pass

