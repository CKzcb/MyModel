#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/2
@File     :   queue_demo
@note     :   
"""

class MyQueue:
    """简单队列"""
    def __init__(self):
        super(MyQueue, self).__init__()
        self.items = []

    def is_empty(self):
        """是否为空"""
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.insert(0, item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)


