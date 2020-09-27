#coding:utf-8
import smtplib
from email.mime.text import MIMEText

class SendEMail(object):
    # 定义第三方 SMTP 服务
    def __init__(self):
        self.mail_host = "smtp.exmail.qq.com"  # SMTP服务器
        self.mail_user = "tech.sys@aa.cn"  # 用户名
        self.mail_pass = "aapwd"  # 密码
        self.sender = 'tech.sys@aa.cn'  # 发件人邮箱
        self.smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
        self.smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证

    def sendmail(self, receivers, title, content):
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(self.sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = title
        try:
            self.smtpObj.sendmail(self.sender, message['To'].split(','), message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)

if __name__ == '__main__':
    sm = SendEMail()
    sm.sendmail(['1093381395@qq.com'], '主题', '正文')
