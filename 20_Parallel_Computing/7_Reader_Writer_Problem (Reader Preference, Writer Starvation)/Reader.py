from threading import Thread

class Reader(Thread):
    def set(self, d, l):
        self.data = d
        self.lock = l


    def run(self):
       while True:
                #locks for read
                self.lock.read_lock()
                    print self.data
                #unlock
                self.lock.read_unlock()

