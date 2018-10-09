from threading import Thread, Lock

queue = []
lock = Lock()

p = Producer()
c = Consumer()

p.set(queue, lock)
c.set(queue, lock)

p.start()
c.start()