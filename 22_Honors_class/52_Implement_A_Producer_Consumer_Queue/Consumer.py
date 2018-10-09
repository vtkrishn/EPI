from threading import Thread, Condition

import random
import time

condition  = Condition()
MAX_NUM = 10

#Producer thread
class Consumer(Thread):
    
    def set(self,q, l):
        self.queue = q
        self.lock = l

    #consume
    def run(self):
        global queue
        while True:
            #get the lock
            #self.lock.acquire()
            condition.acquire()
            if not queue:
                print 'No elements in queue'
                condition.wait()
            #consume the queue data
            num = self.queue.pop(0)
            print 'Consumed :: ', num
            condition.notify()
            #release the lock
            #self.lock.release()
            condition.release()
            time.sleep(random.random())