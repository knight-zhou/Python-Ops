import redis

class ListDB():
    def __init__(self, key):
        self.conn = redis.StrictRedis(host='172.20.128.31', port=6379,decode_responses=True)
        self.key = key

    # 新增数据
    def newData(self, *value, lpush=False):
        """
        :param value: 添加的数据
        :param lpush: boolen, True表示从头部添加数据，默认从尾部添加数据
        :return: 添加后列表的长度
        """
        # if lpush == "lpush":
        #     self.conn.lpush(self.key, *list)
        # elif lpush == "rpush":
        #     self.conn.lpush(self.key, *list)

        # return self.conn.lpush(self.key, *value) if lpush else self.conn.lpush(self.key, *value)
        return self.conn.lpush(self.key, *value)

    # 返回列表中元素的值。index从0开始，当index超出索引时返回null
    def lindex(self, *list):
        return self.conn.lindex(self.key, *list)

    # 查看索引范围内元素的值
    def lrange(self, *data):
        return self.conn.lrange(self.key, *data)

    # 返回列表的长度
    def llen(self):
         return self.conn.llen(self.key)

    # 修改数据
    def lset(self, index, value):
        return self.conn.lset(self.key, index, value)

    # 删除数据
    def deletePop(self, pop=False):
        # if data == "lpop":
        #     return self.conn.lpop(self.key)
        # elif data == "rpop":
        #     return self.conn.rpop(self.key)

        return self.conn.lpop(self.key) if pop else self.conn.rpop(self.key)

if __name__ == '__main__':
    r = ListDB('table_test')
    a = 'a','b'
    r.newData('test', 'vs', lpush = True)
    print("返回列表中元素的值。index从0开始，当index超出索引时返回null: %s" % r.lindex(3))
    r.lset(0,'hello')
    print("查看索引范围内元素的值: {}".format(r.lrange(0, -1)))
    print("返回列表的长度: {}".format(r.llen()))
    r.deletePop(True)
    r.deletePop()
    print("查看索引范围内元素的值: {}".format(r.lrange(0, -1)))


