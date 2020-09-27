#!/usr/bin/env python3
# @Author : knight
import crypt
import getopt
import os
import random
import string
import sys

def getsalt(chars=string.ascii_letters + string.digits):
    return random.choice(chars) + random.choice(chars)


def save(outfile, user, pwd):
    with open(outfile, 'w') as f:
        salt = getsalt()
        f.write(user + ":" + crypt.crypt(pwd, salt))
        f.write("\n")

if __name__ == '__main__':
    output_file = user = password = None  # 定义初始值
    if len(sys.argv) > 1:   
        try:
            opts, _ = getopt.getopt(sys.argv[1:], 'u:p:f:h')
        except getopt.GetoptError as e:
            print("error", e)
            sys.exit(2)

        #print(opts)
        for o, a in opts:
            if o in ('-f'):
                output_file = os.path.abspath(a)
            elif o in ('-u'):
                user = a
            elif o in ('-p'):
                password = a
            elif o in ('-h'):
                print("where options are\n-f filename\n-p password\n-u user")
                exit()
            else:
                assert False, 'unhandled option'

        if all([user, password, output_file]):
            save(outfile=output_file, user=user, pwd=password)
            print("sucess")
        else:
            print("参数不足, 必须要有-f -p -u")

    else:
        print("unhandled option\n"
              "-f filename\n"
              "-p password\n"
              "-u user\n"
              "-h help")
