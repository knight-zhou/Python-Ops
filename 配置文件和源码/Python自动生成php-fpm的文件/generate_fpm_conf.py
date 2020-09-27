#!/usr/bin/env python
"""
	生成php-fpm配置文件脚本 knight.zhou 2020/05/12
	用法:
		python generate_fpm_conf.py -p 监听端口 -a 允许连接的主机IP(默认为127.0.0.1, 多个IP用英文逗号隔开) -P 进程数(默认64)
"""
import sys,getopt,os,socket

config_dir='/etc/php-fpm.d'
log_dir='/home/data/logs/php-fpm'

#帮助信息
def Usage():
    print("""\033[1;33;1mExample:\033[0m
    python {0} -p 9001 -a '10.1.2.12,10.1.2.13'
    -p, --port=<port>\tTCP Listen port
    -a, --allow-list=<host1,host2..,hostN>\tAllow using hosts, Default 127.0.0.1
    -P, --process=<max_children>\t Max process, Default 64""".format(sys.argv[0]))
    print('\n--- PHP-FPM configure file will generate in: /etc/php-fpm.d/www[port].conf\n')
    sys.exit(1)


#获取本机内网IP
def GetlocalIp():
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('8.8.8.8', 0))
		Localip=s.getsockname()[0]
	except:
		Localip='127.0.0.1'
	finally:
		s.close()
	return Localip

#生成配置 
def generate(bind_ip,bind_port,allowlist,children):
	#/etc/php-fpm.d目录不存在会退出
	if not os.path.exists(config_dir):
		print ('\033[1;31;1m{0} can not found.\033[0m'.format(config_dir))
		sys.exit(1)
	#/home/data/logs/php-fpm目录不存在就创建
	if not os.path.exists(log_dir):
		os.makedirs(log_dir)
	#给/home/data/logs/php-fpm wwwuser可写
	Cmd='chown wwwuser.wwwuser {0}'.format(log_dir)
	Result=os.system(Cmd)
	ConfigFile='{0}/wwwuser{1}.conf'.format(config_dir,bind_port)
	Template="""[www{0}]
listen = {1}:{0}
listen.allowed_clients = {3}
user = wwwuser 
group = wwwuser
pm = static
pm.max_children = {4}
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 35
pm.max_requests = 1024
request_terminate_timeout = 300
request_slowlog_timeout = 3
slowlog = /home/data/logs/php-fpm/www{0}-slow.log
rlimit_files = 65535
rlimit_core = 0
php_admin_value[error_log] = /home/data/logs/php-fpm/www{0}-error.log
php_flag[display_errors] = off
php_admin_flag[log_errors] = on
php_value[session.save_handler] = files
php_value[session.save_path]    = /var/lib/php/session
""".format(bind_port,bind_ip,bind_port,allowlist,children,bind_port,bind_port)
	print('\033[1;33;2mPreview:\033[0m\n{0}'.format(Template))
	#写入文件
	f=open(ConfigFile,'w')
	f.write(Template)
	f.close()
	print ("Generate file: \033[1;32;5m{0} success.\033[0m".format(ConfigFile))
#参数个数检查
if len(sys.argv) < 3 or len(sys.argv) > 7:
        Usage()

#初始化参数
Port=''
AllowList='127.0.0.1'  #允许请求该服务的主机，如果未指定的话默认127.0.0.1
Process=64   #fastcgi进程数，如果未指定的话默认64

#输入参数处理
opts,args=getopt.getopt(sys.argv[1:],"p:a:P:",["port=","allow-list=","process="])
for op,value in opts:
        if op in ("-p","--port"):
                Port = value.lstrip()
        elif op in ("-a","--allow-list"):
                AllowList = '%s,%s' % (AllowList,value.lstrip())
        elif op in ("-P","--process"):
                Process = value.lstrip()
        else:
                Usage()
#执行生成
generate(bind_ip=GetlocalIp(),bind_port=Port,allowlist=AllowList,children=Process)

