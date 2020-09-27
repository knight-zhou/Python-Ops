from RedisHelper import RedisHelper
obj = RedisHelper()

#调用订阅方法
redis_sub = obj.subscribe()
#写一个死循环，持续输出订阅内容
while True:
    msg =  redis_sub.parse_response()
    print(msg)