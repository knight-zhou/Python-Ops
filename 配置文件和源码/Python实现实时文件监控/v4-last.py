#!/usr/bin/env python
import pyinotify
import time
import os
from S_mail import SendEMail


## 定义变量
key_word="wechat"

class ProcessTransientFile(pyinotify.ProcessEvent):
  def process_IN_MODIFY(self, event):
    line = file.readline()
    if key_word in line:
      print("有{0},发送告警".format(key_word))
      sm = SendEMail()
      sm.sendmail(['xx@qq.com'], '主题', '正文')
     

filename = '/media/tmp/pay-api_error.log'
file = open(filename,'r')

#找到文件的大小并移动到末尾
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)
wm.watch_transient_file(filename, pyinotify.IN_MODIFY, ProcessTransientFile)

notifier.loop()