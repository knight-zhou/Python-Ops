import crypt
import sys
import random,string

if len(sys.argv) != 4:
    print("Usages: {0} [user|psssword|file_name]".format(sys.argv[0]))
    sys.exit(1)


user = sys.argv[1]
pwd = sys.argv[2]
file_name = sys.argv[3]

def getsalt(chars = string.ascii_letters+string.digits):
    return random.choice(chars)+random.choice(chars)

# salt = getsalt()
# print(crypt.crypt(pwd,salt))

# 写入文件
with open(file_name,'w') as f:
    salt = getsalt()
    print("sucess")
    f.write(user+":"+crypt.crypt(pwd,salt))
    f.write("\n")