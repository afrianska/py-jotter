from queue import Queue

q = Queue()

q.enqueue("hello")
print(q.size())

q.enqueue("dog")
print(q.size())

q.enqueue(3)
print(q.size())

q.dequeue()
print(q.size())
