"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(selfs):
        return selfs.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
     q = Queue()
     print(q)
     print(q.is_empty())
     q.enqueue(1)
     q.enqueue(2)
     q.enqueue(3)
     print(q)
     print(q.size())
     print(q.peek())
     print(q.dequeue())
     print(q)