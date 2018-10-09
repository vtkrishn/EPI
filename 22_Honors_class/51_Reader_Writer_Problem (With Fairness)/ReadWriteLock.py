from threading import Lock
class ReadWriteLock(Lock):
    reader = 0
    writer = 0
    condition = Condition()
    
    def read_lock(self):
        while writer > 0:
            condition.wait()
        if reader >= 0:
            condition.acquire()
            reader +=1
    
    def read_unlock(self):
        if reader > 0:
            reader -= 1
        condition.notify()
        condition.release()
    
    def write_lock(self):
        while reader > 0 || writer > 0:
            condition.wait()
        condition.acquire()
        writer += 1

    def write_unlock(self):
        if writer > 0:
            writer -= 1
        condition.notify()
        condition.release()
            
