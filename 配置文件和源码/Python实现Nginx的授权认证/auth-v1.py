import crypt
import random,string

def getsalt(chars = string.ascii_letters+string.digits):
    return random.choice(chars)+random.choice(chars)

## 调试
# print(string.ascii_letters)  # 输出字母表
# print(string.digits)  #输出0-9的数字
# random.choice("xx")  # 返回随机数
#print(getsalt())

# 函数赋值给变量
salt = getsalt()
#输出加密内容
print(crypt.crypt('knight111',salt))