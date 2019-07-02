#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/2
@File     :   double_queue
@note     :   
"""

class Deque:
    """双端队列"""
    def __init__(self):
        super(Deque, self).__init__()
        self.items = []

    def is_empty(self):
        """是否为空"""
        return self.items == []

    def add_front(self, item):
        """在队列的头插入元素"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """在队尾插入元素"""
        self.items.append(item)

    def remove_front(self):
        """从对头出元素"""
        return self.items.pop(0)

    def remove_rear(self):
        """从队尾出元素"""
        return self.items.pop()

    def size(self):
        """队列大小"""
        return len(self.items)


if __name__ == '__main__':
    test = Deque()
    test.add_front(1)
    test.add_front(2)
    test.add_rear(3)
    test.add_rear(4)
    print(test.size())
    print(test.remove_front())
    print(test.remove_front())
    print(test.remove_rear())
    print(test.remove_rear())

