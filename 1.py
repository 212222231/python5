from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 右击操作（新闻）
right_click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a[1]")
ActionChains(driver).context_click(right_click).perform()

# 悬停操作（设置）
# on_stop = driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
# ActionChains(driver).move_to_element(on_stop).perform()



sleep(1)
driver.quit()