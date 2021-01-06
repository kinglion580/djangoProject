import time

from test_queue import RedisQueue


q = RedisQueue('rq')  # 新建队列名为rq
for i in range(5):
    q.put(i)
    print("input.py: data {} enqueue {}".format(i, time.strftime("%c")))
    time.sleep(1)