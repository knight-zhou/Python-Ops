# coding:utf-8
import subprocess
import argparse
import os
"""
python jar.py -list "test"

"""

try:
    import json
except ImportError:
    import simplejson as json


def jarList():
    command = "ps -ef |grep java|grep -v grep|grep '1.0.0.jar'|awk '{print $NF}'"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    port_list = p.stdout.read().split('\n')
    port = []
    for i in port_list:
        if len(i) != 0:
            port += [{'{#JAVAPSS}': i}]
    print(json.dumps({'data': port}, sort_keys=True, indent=4, separators=(',', ':')))


##获取对应的jar包的pid值
def getpid(name):
    pid=os.popen("ps -ef | grep  {0}|grep -v grep".format(name)).readlines()[0].split()[1]
    return pid


def cpuinfo(pid):
    command = "ps -p {0} -o pcpu".format(pid)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    xx=p.stdout.read().split('\n')
    res=int(float(xx[1]))
    print(res)
    return res
###
parser = argparse.ArgumentParser()
parser.add_argument("-l","--list", help="list jar process")
parser.add_argument("-n","--name", help="java name")
parser.add_argument("-c","--cpu", help="count for cpu value")
args = parser.parse_args()

if args.list:
    jarList()
elif args.name and args.cpu == "cpu":
    cpuinfo(getpid(args.name))

