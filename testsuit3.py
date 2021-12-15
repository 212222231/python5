import unittest
# 导入生成html格式测试报告的库
from Commonlib.HTMLTestRunner import HTMLTestRunner
from Testcase import login
# from Testcase import login,add_Warehouse,add_supplier,add_drugs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


# 创建测试套件
mysuit = unittest.TestSuite()
mysuit.addTest(unittest.makeSuite(login.Testcase))
# mysuit.addTest(unittest.makeSuite(add_supplier.Testcase))
# mysuit.addTest(unittest.makeSuite(add_Warehouse.Testcase))
# mysuit.addTest(unittest.makeSuite(add_drugs.Testcase))

# 生成html格式测试报告的步骤
with open('report12.17.html','wb')as f:
        HTMLTestRunner(
            stream=f,
            title='进销存系统报告',
            description='登录、新建供货商、仓库模块',
             verbosity=2
        ).run(mysuit)

def send_mail():
    '''
    发送测试报告到邮箱
    :param report_name: 需要发送的测试报告
    :param receiver: 邮件接收人
    :return:
    '''
    # ----------------------------------------------------------
    # 获取邮件正文,读取测试报告的内容
    f = open('C:\\Users\\A\\Desktop\\my\\进销存python\\report12.17.html', 'rb')
    mail_body = f.read()
    f.close()
    # 邮件服务器
    smtpserver = 'smtp.qq.com'
    # 发件人和密码
    sender = '1514743177@qq.com'
    password = 'vwcvjckszcmijaii'
    # 接收人
    receiver = '1514743177@qq.com'
    # 邮件主题
    subject = '进销存测试报告'
    # ----------------------------------------------------------
    # 连接登录邮箱
    server = smtplib.SMTP(smtpserver, 25)
    server.login(sender, password)
    # ----------------------------------------------------------
    # 添加附件
    sendfile = open('C:\\Users\\A\\Desktop\\my\\进销存python\\report12.17.html', 'rb').read()
    att = MIMEText(sendfile, "base64", 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    msg = MIMEMultipart('related')
    msgtext = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgtext)
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg.attach(att)
    # ----------------------------------------------------------
    # 发送邮件
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()
    print("发送成功!")

send_mail()



if __name__ == '__main__':
    unittest.main()
