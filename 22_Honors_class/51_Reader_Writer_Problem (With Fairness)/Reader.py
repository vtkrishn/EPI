from threading import Thread

class Reader(Thread):
    def set(self, d, l):
        self.data = d
        self.lock = l


    def run(self):
       while True:
                self.lock.read_lock()
                    print self.data
                self.lock.read_unlock()

