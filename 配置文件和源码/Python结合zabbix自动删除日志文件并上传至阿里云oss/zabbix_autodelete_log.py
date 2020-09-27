# -*- coding: utf-8 -*-
import oss2
import subprocess
import socket
import os

#定义变量
cmd = "find /home/data/logs/ -type f -mtime +15"
hostname = socket.gethostname()

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('B2Cx4K80gPDQlhP5', 'xx')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'knight-oss-hz')

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
file = p.stdout.readlines()


# 生成历史文件路径的列表
log_list=[]
for line in file:
    line=line.rstrip("\n")
    log_list.append(line)

# 定义删除日志文件函数
def del_log():
    cmd = "find /home/data/logs/ -type f -mtime +1|xargs rm -rf"
    os.system(cmd)


# 定义上传文件函数
def upload_file():
    for log_file_path in log_list:
        log_file_name = log_file_path.split("/")[-1]
        bucket.put_object_from_file('{0}/{1}'.format(hostname, log_file_name), log_file_path)


if __name__ == '__main__':
    # 先上传文件
    upload_file()
    # 再删除历史文件
    del_log()
