from queue import Queue

# FIFO (first input first output)
q = Queue(maxsize=3)

q.put('item1')
q.put('item2')
q.put('item3')

print(q.empty())
print(q.full())
