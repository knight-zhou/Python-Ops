#!/usr/bin/python
#coding:utf-8
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from collections import namedtuple

# 用来加载解析yaml文件或JSON内容,并且支持vault的解密
loader = DataLoader()
inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])    # 指定host文件

## 管理变量的类,包括主机,组,扩展等变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

#初始化需要的对象
Options = namedtuple ('Options',
                     ['connection',
                      'remote_user',
                      'ask_sudo_pass',
                      'ack_pass',
                      'module_path',
                      'forks',
                      'become',
                      'become_method',
                      'become_user',
                      'check',
                      'listhosts',
                      'sudo_user',
                      'sudo',
                      'diff']
                     )

#定义连接远端的方式为smart
options = Options(connection='smart',
                  remote_user='root',
                  ack_pass=None,
                  sudo_user=None,
                  forks=5,
                  ask_sudo_pass=None,
                  module_path=None,
                  become=None,
                  become_method=None,
                  become_user=None,
                  listhosts=None,
                  check=False,
                  diff=False,
                  sudo=False)

play_source = dict(
    name = 'exec shell', #任务名称
    #hosts = '10.20.128.21', # 目标主机
    hosts = 'all', # 目标主机
    gather_facts = 'yes', # 获取主机基本信息
    tasks = [
        dict(action=dict(module='shell', args='hostname')),
    ]
)
# 执行任务
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

## 使用密码验证
passwords = None   # 定义初始密码为空
passwords = dict(conn_pass='zhoulong')
#variable_manager.extra_vars={"ansible_user": "www", "ansible_ssh_pass": "zhoulong"}

## 定义任务队列
tqm = TaskQueueManager(
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    options=options,
    passwords=passwords
)
##
result = tqm.run(play)
print(result)
