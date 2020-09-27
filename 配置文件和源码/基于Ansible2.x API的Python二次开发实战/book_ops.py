#!/usr/bin/python
#coding:utf-8
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from collections import namedtuple
from ansible.executor.playbook_executor import PlaybookExecutor


"""
exec_shell:
    # 任务名称
    # 目标主机
    # module="shell"
    # args='touch /media/bbb.log'

"""
## 封装api供外部调用
class OpsManager(object):
    def __init__(self,passwords = dict(ansible_user='www',conn_pass='zhoulong')):
	    self.passwords=passwords

        # 用来加载解析yaml文件或JSON内容,并且支持vault的解密
        self.loader = DataLoader()


        # 根据inventory加载对应变量
        self.inventory = InventoryManager(loader=self.loader,sources=['/etc/ansible/hosts'])
        self.variable_manager = VariableManager(loader=self.loader,inventory=self.inventory)

        # 初始化需要的对象
        self.Options = namedtuple('Options',
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
                      	      'listtasks',
                              'listtags',
                              'syntax',
                              'sudo_user',
                              'sudo',
                              'diff']
                             )

        # 定义连接远端的方式为smart
        self.options = self.Options(connection='smart',
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
	                  listtasks=None,
                  	  listtags=None,
                          syntax=False,
                          check=False,
                          diff=False,
                          sudo=False)

        ## 定义任务队列
        self.tqm = TaskQueueManager(
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            options=self.options,
            passwords=self.passwords
        )



    def runjob(self,taskname,host_list,module,args):
        play_source = dict(
            name=taskname,  
            hosts=host_list,  
            gather_facts='yes',
            tasks=[
                dict(action=dict(module=module, args=args)),
            ]
        )

        # 执行任务(shell)
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)

        # 使用密码认证
        passwords = self.passwords

        # 执行并输出
        result = self.tqm.run(play)
        return result

    def runplaybook(self,bookyml,extra_vars):
        playbook = PlaybookExecutor(playbooks=[bookyml],
                                    inventory=self.inventory,
                                    variable_manager=self.variable_manager,
                                    loader=self.loader,
                                    options=self.options,
                                    passwords=self.passwords)
	# 设置变量
	#self.variable_manager.extra_vars = {'hosts':'all','xx':'yy'}      # 设置变量传入
	self.variable_manager.extra_vars = extra_vars
        playbook.run()



if __name__ == '__main__':
    opsmanager=OpsManager()
    #opsmanager.runjob("exe shell","all","shell","touch /tmp/xxoo")
    opsmanager.runplaybook("/etc/ansible/playbook/xx.yml",extra_vars={'hosts':'all'})
