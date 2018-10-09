data = []
lock = Lock()

r = Reader()
w = Writer()

r.set(data, lock)
w.set(data, lock)

r.start()
w.start()