#!/usr/bin/env python3
from optparse import OptionParser
import crypt
import random,string

# 定义函数
def getsalt(chars = string.ascii_letters+string.digits):
    return random.choice(chars)+random.choice(chars)

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",help="write report to file", metavar="FILE")
parser.add_option("-u", "--user", dest="user",type="string",help="it is user")
parser.add_option("-p", "--password", dest="pwd",help="it is passord")

(options, args) = parser.parse_args()

with open(options.filename,'w') as f:
    salt = getsalt()
    print("sucess")
    f.write(options.user+":"+crypt.crypt(options.pwd,salt))
    f.write("\n")
