import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_mail():
    '''
    发送测试报告到邮箱
    :param report_name: 需要发送的测试报告
    :param receiver: 邮件接收人
    :return:
    '''
    # ----------------------------------------------------------
    # 获取邮件正文,读取测试报告的内容
    f = open('D:\\my\\进销存python\\report11.27.html', 'rb')
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
    sendfile = open('D:\\my\\进销存python\\report11.27.html', 'rb').read()
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