import time
from queue import Queue
from threading import Thread

# 创建一个队列
q = Queue()

class Producer(Thread):
    """生产者"""

    def run(self):
        # 判断队列中的商品数是否少于50，少于50了之后就生产200个
        count = 0
        while True:
            if q.qsize()<50:
                for i in range(200):
                    count += 1
                    goods = '--第{}个商品---'.format(count)
                    q.put(goods)
                    print("生产：",goods)
            time.sleep(1)

class Consumer(Thread):
    """消费者"""
    def run(self):
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    print('消费：{}'.format(q.get()))
            else:
                time.sleep(2)

p = Producer()
p.start()

for i in range(5):
    c = Consumer()
    c.start()














