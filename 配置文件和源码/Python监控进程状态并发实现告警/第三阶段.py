# coding:utf-8
import smtplib
from email.mime.text import MIMEText
import psutil

# 定义第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # SMTP服务器
mail_user = "tech.sys@aa.cn"  # 用户名
mail_pass = "aapwd"  # 密码
sender = 'tech.sys@aa.cn'  # 发件人邮箱
receivers = ['yy@qq.com','xx@qq.com']  ## 多个邮箱用逗号隔开构成列表

# 定义进程名
P_name = "node_exporter"

#邮件发送函数
def SendMail(receivers,title,content):
    # content = '这是正文'
    # title = '这是主题'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, message['To'].split(','), message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

#定义检测进程函数
def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid
##
# SendMail(receivers,"主题","正文2")

if isinstance(checkprocess(P_name),int):
    pass   # 进程存在
else:
    print("{0}进程不存在,发送邮件".format(P_name))
    SendMail(receivers,"{0}进程down掉了".format(P_name),"{0}进程down掉了，请检测原因....".format(P_name)