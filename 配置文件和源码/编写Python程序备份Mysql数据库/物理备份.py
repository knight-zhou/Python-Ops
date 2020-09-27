# coding:utf-8
import os
import subprocess
import sys
import time

#定义服务器，用户名、密码和备份的路径
DB_HOST = 'localhost'
DB_USER = 'bkpuser'
DB_USER_PASSWD = '123456'
BACKUP_PATH = '/home/data/dbbackup/xtra'

#定义日志文件路径
DATETIME = time.strftime('%Y%m%d')
LOG_PATH="/home/data/logs/xtra/{0}".format(DATETIME)

print("开始创建备份文件夹,如果不存在就创建....")
#创建备份文件夹
if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)

print("开始创建日志文件夹,如果不存在就创建....")
##创建备份文件夹
if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

#删除历史的备份
def cleanstore():
    command = "find %s -type d -mtime +15 |xargs rm -rf" %BACKUP_PATH
    subprocess.call(command, shell=True)

def backupfull():
    commandfull="innobackupex --defaults-file=/etc/my.cnf --user={0} --password={1} /home/data/dbbackup/xtra/".format(DB_USER,DB_USER_PASSWD)
    #subprocess.call(commandfull, shell=True)
    subprocess.call(commandfull, shell=True,stdout=open('{0}/xtra.log'.format(LOG_PATH),'w'),stderr=subprocess.STDOUT)  # 标准输出存日志


if __name__ == '__main__':
    cleanstore()
    backupfull()
    sys.exit(0)
