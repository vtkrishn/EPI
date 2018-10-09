from threading import Thread,Condition
import random
import time

#Producer thread
condition  = Condition()
MAX_NUM = 10

class Producer(Thread):
    
    def set(self,q, l):
        self.queue = q
        self.lock = l

    #produce
    def run(self):
        nums = range(5) #creates [0,1,2,3,4]
        while True:
            #get the lock
            #self.lock.acquire()
            condition.acquire()
            if len(self.queue) == MAX_NUM:
                print 'queue size is full'
                condition.wait()
                print 'waiting for consumers to take from queue'
            num  = random.choice(nums) #pick random from choices
            #modify the queue with the produced number
            self.queue.append(num)
            print 'Produced :: ', num
            condition.notify()
            #release the lock
            #self.lock.release()
            condition.release()
            time.sleep(random.random())