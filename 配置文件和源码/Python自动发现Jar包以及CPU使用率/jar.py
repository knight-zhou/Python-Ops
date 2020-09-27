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


##
parser = argparse.ArgumentParser()
parser.add_argument("-l","--list", help="list jar process")
args = parser.parse_args()

if args.list:
    jarList()