import redis

class RedisHelper():
    def __init__(self):
        self.__conn = redis.Redis(host='172.20.128.31', port=6379)
        self.channel = 'monitor'  # 定义名称

    def publish(self, msg):  # 定义发布方法
            self.__conn.publish(self.channel, msg)
            return True

    def subscribe(self):  # 定义订阅方法
            pub = self.__conn.pubsub()
            pub.subscribe(self.channel)
            pub.parse_response()
            return pub
