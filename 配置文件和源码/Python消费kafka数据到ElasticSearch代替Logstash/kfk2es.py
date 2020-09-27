from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time
from multiprocessing import Process

# 计算当前的时间
l_date = time.strftime("%Y.%m.%d", time.localtime())
local_date=str(l_date)

boot_server=['172.20.128.31:9092']
## 读kafka数据
consumer = KafkaConsumer('javadaemon',group_id="py-consumer",bootstrap_servers=boot_server)

##读es
es = Elasticsearch('http://172.20.128.31:9200')

## 定义kafka到elastic的函数
def kfk2es(consumer):
    for msg in consumer:
        j_data = msg.value.decode('utf-8')  # 流编码成utf-8字符串
        dict_data = json.loads(j_data)
        index_1 = dict_data["log"]["file"]["path"]
        index_2 = index_1.split("/")[4]
        index = index_2 + "-" + dict_data["topic"] + "-" + local_date
        ## 先判断有没有索引,没有就创建日期类的索引
        aa = es.indices.exists(index=index)
        print(dict_data)
        print("索引是:" + index)
        if aa:
            print("索引存在...不需要再创建了")
        else:
            print("创建索引")
            res = es.indices.create(index=index)
        # 读取kafka的数据写入elastic
        es.index(index=index, doc_type="_doc", body=dict_data)


#开启多进程
p1=Process(target=kfk2es,args=(consumer,)) #必须加,号
p2=Process(target=kfk2es,args=(consumer,))
p3=Process(target=kfk2es,args=(consumer,))

p1.start()
p2.start()
p3.start()
print('主线程')
