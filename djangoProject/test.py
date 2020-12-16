import queue

q = queue.Queue()

q.put('a')
q.put('b')
q.get()
q.put('c')
q.get()
q.get()
q.get()
q.get()
q.put('d')
q.put('e')
q.put('f')
