"""
-------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 17:16
# @Author  : fanqian
# @File    : Base.py
# @IDE     : PyCharm
-------------------------------------------------------------
"""

from util.Log import Log
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
import unittest,time,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from util.config import IMG_PATH,get_time

class Base(unittest.TestCase):
	def setUp(self):
		print("--------------开始执行用例--------------")

	def tearDown(self):
		print("--------------用例执行结束--------------")

	@classmethod
	def setUpClass(cls):
		os.system("taskkill /im chromedriver.exe /f")
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(15)
		get_time()

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def find_element(self, loc):
		"""
		定位单个元素
		:param loc:元素的属性
		:return:
		"""
		try:
			element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*loc))
		except (NoSuchElementException, TimeoutException) as e:
			raise e
		else:
			return element

	def find_elements(self, loc):
		"""
		定位一组元素
		:param loc:元素相同的属性
		:return:
		"""
		try:
			elements = WebDriverWait(self.driver, 30).until(lambda x: x.find_elements(*loc))
		except (NoSuchElementException, TimeoutException) as e:
			raise e
		else:
			return elements

	def get_url(self,url):
		"""
		打开URL
		:param url:URL地址
		:return:
		"""
		self.driver.get(url)

	def clear_key(self, loc):
		"""
		清空输入框
		:param loc:输入框元素
		:return:
		"""
		time.sleep(3)
		self.find_element(loc).clear()

	def send_keys(self, loc, value):
		"""
		输入内容
		:param loc:输入框元素
		:param value: 输入内容
		:return:
		"""
		self.clear_key(loc)
		self.find_element(loc).send_keys(value)

	def click_button(self, loc):
		"""
		点击按钮
		:param loc:按钮元素
		:return:
		"""
		self.find_element(loc).click()

	def save_img(self, img_name):
		"""
		截图
		:param img_name:图片名称
		:return:
		"""
		img_path = IMG_PATH+'\\'+img_name+'.png'
		print(img_path)
		self.driver.get_screenshot_as_file(img_path)

	def hover(self, el, time_to_hover=1):
		"""
		悬停
		:param time_to_hover:
		:param el: 一个元素
		"""
		ActionChains(self.driver).move_to_element(el).perform()
		time.sleep(time_to_hover)




