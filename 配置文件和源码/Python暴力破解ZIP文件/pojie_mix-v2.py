import itertools as its
import zipfile
import sys

## 接收传进来的参数;
xx_num = sys.argv[1]

##判断传入的参数个数
if len(sys.argv) != 2:
    print("请猜测密码的位数,传入一个变量即可")
    sys.exit(1)

## 判断传入的是否是数字
if  xx_num.isdigit():
    xx_num=int(xx_num)
else:
    print("请传入数字")
    sys.exit(1)

##定义原始字符集合
word = "abc123"
## 定义一个空列表用于放置这些字典
list_data=[]

## 定义解压函数
def unzip_file(src_file,des_file,password):
    '''
    解压单个文件到目标文件夹
    '''
    if password:
        password=str(password)
        password= password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=des_file,pwd=password)
        return 0
    except RuntimeError as e:
        # print(e)
        return -1
    finally:
        zf.close()

def produce_data(num):
    r = its.product(word, repeat=num)
    for line in r:
        line1 = "".join(line)
        list_data.append(line1)


## 猜测密码是4位
produce_data(xx_num)

# 穷举破解
for line in list_data:
    try:
        code = unzip_file("xx.zip",'.',line)
        if code != -1:
            print('爆破成功,密码是:{0}'.format(line))
            break
    except:
        pass
