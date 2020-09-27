from RedisHelper import RedisHelper
import time

#实例化
obj = RedisHelper()


for i  in range(50):
    obj.publish("Hello-{0}".format(i))
    time.sleep(5)
