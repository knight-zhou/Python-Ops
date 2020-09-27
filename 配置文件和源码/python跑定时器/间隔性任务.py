# coding:utf-8
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('现在的时间是: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()   
    scheduler.add_job(tick, 'interval', seconds=3)  # 间隔三秒执行

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
