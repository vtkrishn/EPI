from threading import Lock
class ReadWriteLock(Lock):
    reader = 0
    writer = 0
    condition = Condition()
    
    def read_lock(self):
        #if there are more than one writer then wait
        while writer > 0:
            condition.wait()
        #if there are more readers then increment the counter
        if reader >= 0:
            #acquire the lock
            condition.acquire()
            #increment
            reader +=1
    
    def read_unlock(self):
        #if there are more than one reader then decrement the reader
        if reader > 0:
            reader -= 1
        #notify
        condition.notify()
        #release the lock
        condition.release()
    
    def write_lock(self):
        #if there are more than one reader or writer then wait
        while reader > 0 || writer > 0:
            condition.wait()
        #acquire write lock
        condition.acquire()
        #increment
        writer += 1

    def write_unlock(self):
        #if there are more than one writer decrement
        if writer > 0:
            writer -= 1
        #notify
        condition.notify()
        #release the lock
        condition.release()
            
