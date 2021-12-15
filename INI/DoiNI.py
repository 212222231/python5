import configparser
# 读取配置文件
# cf = configparser.ConfigParser()
# # 读取config.int文件
# cf.read("config.ini")
# def getConfigValue(section,name):
#     value = cf.get(section,name)
#     return value
# BaiduUrl = getConfigValue("url","baidu")
# print(BaiduUrl)

# # 写入ini文件，添加节
# cf.add_section("title")
# cf.set("title","name","HelloWorld!")
# cf.write(open("config.ini","w"))
#
# try:
#     cf.add_section("title")
#     cf.set("title","name","HelloWorld!")
#     cf.set("title","name1","HelloWorld1!")
#     cf.set("title","name2","HelloWorld2!")
#
# except configparser.DuplicateOptionError:
#     print("Section 'title' already exists!")
#
# cf.write(open("config.ini","w"))


# 将读取配置文件的操作封装在类中
class ReadConfigIni():
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)
    def getConfigValue(self,section,name):
        value = self.cf.get(section,name)
        return value

DoConfigIni = ReadConfigIni("config.ini")
BaiUrl = DoConfigIni.getConfigValue("url","baidu")
print(BaiUrl)
