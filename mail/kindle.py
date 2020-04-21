#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

my_sender=   # 发件人邮箱账号
my_pass =               # 发件人邮箱密码
my_user=      # 收件人邮箱账号
def mail():
    # ret=True
    # try:
    # msg=MIMEText('','plain','utf-8')
    msg = MIMEMultipart()
    msg['From']=formataddr(["kindle_sender",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="kindle文件"                # 邮件的主题，也可以说是标题
    # 构造附件1，传送当前目录下的 test.txt 文件

    att1 = MIMEText(open('/media/plan/如何阅读一本书-328c.mobi', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="阅读一本书.mobi"'


    msg.attach(att1)
    server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    # except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        
    #     ret=False
    # return ret
    

ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")