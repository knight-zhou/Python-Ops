# coding:utf-8
from configparser import ConfigParser
cfg = ConfigParser()
cfg.read("abc.ini")

cfg.remove_section('ip.yeyese.club') #删除section
cfg.remove_option('csdn.net',"user") #删除一个配置想

# 重新写入配置当中去
with open('abc.ini','w') as f:
    cfg.write(f)