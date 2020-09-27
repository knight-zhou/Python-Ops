# coding:utf-8
from S_mail import SendEMail   #导入邮件类
import psutil
# 实例化邮件类
sm = SendEMail()

## 定义收件人
receivers = ['1093381395@qq.com','xx@qq.com']  # 接收人邮箱
# 定义进程名
P_name="node_exporter"


#定义检测进程函数
def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid

if isinstance(checkprocess(P_name),int):
    pass   # 进程存在
else:
    print("{0}进程不存在,发送邮件".format(P_name))
    sm.sendmail(receivers,"{0}进程down掉了".format(P_name),"{0}进程down掉了，请检测原因....".format(P_name))