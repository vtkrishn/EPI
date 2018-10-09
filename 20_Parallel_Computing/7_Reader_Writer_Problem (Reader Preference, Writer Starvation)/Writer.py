import random
class Writer(Thread):

    def set(self, d, l):
        self.data = d
        self.lock = l

    def run(self):
        while True:
            #locks for write
            self.lock.write_lock()
            #generate data
            self.data.append(random.choice([0,1,2,3,4]))
            #unlock
            self.lock.write_unlock()