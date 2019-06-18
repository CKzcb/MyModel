#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/6/18
@File     :   stack
@note     :   栈
"""

class Stack:
    """栈类"""
    def __init__(self):
        super(Stack, self).__init__()
        # 保存栈元素
        self._items = []

    def is_empty(self):
        """
        是否为空栈
        :return:
        """
        return len(self._items) == 0

    def push(self, item):
        """
        放入元素
        :param item:需要放入的元素
        :return:
        """
        self._items.append(item)

    def pop(self):
        """
        弹出元素
        :return:被弹出的元素
        """
        return self._items.pop()

    def peek(self):
        """
        返回栈顶元素
        :return:栈顶元素
        """
        return self._items[-1] if len(self._items) > 0 else None

    def size(self):
        """
        返回栈的大小
        :return:栈中元素个数
        """
        return len(self._items)


if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

