#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/6/18
@File     :   structs_double_link_list
@note     :   双向链表
"""

class Node:
    """节点类"""
    def __init__(self, item):
        super(Node, self).__init__()
        self.item = item
        self.next = None
        self.prev = None


class DoubLinkList:
    """双向链表"""
    def __init__(self):
        super(DoubLinkList, self).__init__()
        self._head = None

    def is_empty(self):
        """
        链表是否为空
        :return:
        """
        return self._head == None

    def length(self):
        """
        返回链表的长度
        :return: 链表长度
        """
        tmp_cur = self._head
        count = 1
        while tmp_cur.next != None:
            count += 1
            tmp_cur = tmp_cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        tmp_cur = self._head
        while tmp_cur != None:
            print(tmp_cur.item)
            tmp_cur = tmp_cur.next

    def add(self, item):
        """
        头部插入元素
        :param item:需要插入的元素
        :return: is_result : 是否成功，失败进行回滚
        """
        is_result = True
        tmp_node = Node(item)
        # 如果是空链表，将_head指向node
        if self.is_empty():
            self._head = tmp_node
        else:
            # 将新节点指向头结点
            tmp_node.next = self._head
            # 将头结点的前指针指向新节点
            self._head.prev = tmp_node
            self._head = tmp_node
        return is_result

    def append(self, item):
        """
        尾部追加
        :param item:需要添加的元素
        :return: 是否成功
        """
        is_result = True
        tmp_node = Node(item)
        # 为空则直接加入新节点
        if self.is_empty():
            self._head = tmp_node
        else:
            # 循环遍历到最后一个节点
            tmp_cur = self._head
            while tmp_cur.next != None:
                tmp_cur = tmp_cur.next
            # 当前节点指向新节点
            tmp_cur.next = tmp_node
            # 新节点前指针指向当前节点
            tmp_node.prev = tmp_cur
        return is_result

    def insert(self, pos, item):
        """
        指定位置插入元素
        :param pos: 位置
        :param item: 需要插入的元素
        :return: 是否成功
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            tmp_node = Node(item)
            tmp_cur = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                tmp_cur = tmp_cur.next
            tmp_node.prev = tmp_cur
            tmp_node.next = tmp_cur.next
            tmp_cur.next.prev = tmp_node
            tmp_cur.next = tmp_node

    def search(self, item):
        """
        查找元素是否存在
        :param item: 需要查找的元素
        :return: True : False 是否存在
        """
        is_result = False
        tmp_cur = self._head
        while tmp_cur.next != None:
            if tmp_cur.item == item:
                is_result = True
                break
            tmp_cur = tmp_cur.next
        else:
            if tmp_cur.item == item:
                is_result = True
        return is_result

    def remove(self, item):
        """
        删除元素
        :param item: 要删除的元素
        :return: is_result : 是否删除成功
        """
        is_result = False
        # 为空则删除失败
        if self.is_empty():
            return is_result
        tmp_cur = self._head
        # 第一个节点为要删除的元素
        if tmp_cur.item == item:
            if tmp_cur.next == None:
                self._head = None
            else:
                tmp_cur.next.prev = None
                self._head = tmp_cur.next
            return is_result
        while tmp_cur != None:
            # 找到要删除的元素，把指针断开
            if tmp_cur.item == item:
                tmp_cur.prev.next = tmp_cur.next
                tmp_cur.next.prev = tmp_cur.prev
                is_result = True
                break
            tmp_cur = tmp_cur.next
        return is_result



if __name__ == "__main__":
    ll = DoubLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(4))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()






