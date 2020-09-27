# coding:utf-8
import os
import time
#定义服务器，用户名、密码、数据库名称和备份的路径
DB_HOST = 'localhost'
DB_USER = 'backup'
DB_USER_PASSWD = '123456'
DB_NAME = 'test'
BACKUP_PATH = '/home/data/dbbackup/mysql/'

DATETIME = time.strftime('%Y%m%d-%H%M')
TODAYBACKUPPATH = BACKUP_PATH + DATETIME

print("开始创建备份文件夹,如果不存在就创建....")
#创建备份文件夹
if not os.path.exists(TODAYBACKUPPATH):
        os.makedirs(TODAYBACKUPPATH)

# 创建备份函数
def run_backup():
    dumpcmd = "mysqldump -u" + DB_USER + " -p" + DB_USER_PASSWD + " " + DB_NAME + " > " + TODAYBACKUPPATH + "/" + DB_NAME + ".sql"
    os.system(dumpcmd)

#执行压缩的函数
def run_tar():
        compress_file = TODAYBACKUPPATH + ".tar.gz"
        compress_cmd = "tar -czvf " +compress_file+" "+DATETIME
        os.chdir(BACKUP_PATH)
        os.system(compress_cmd)
        print("压缩已完成......")
        #删除备份文件夹
        remove_cmd = "rm -rf "+TODAYBACKUPPATH
        os.system(remove_cmd)

## 开始备份数据库
if __name__ == '__main__':
    run_backup()
    run_tar()