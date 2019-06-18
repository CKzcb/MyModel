#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/6/17
@File     :   structs_signal_cyc_link_list
@note     :   单向循环链表
"""

class Node:
    """节点类"""
    def __init__(self, item):
        super(Node, self).__init__()
        self.item = item
        self.next = None


class SignalCycLinkList:
    """单向循环链表"""
    def __init__(self):
        super(SignalCycLinkList, self).__init__()
        self._head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return: True False
        """
        return self._head == None

    def length(self):
        """
        获取链表的长度
        :return: 链表长度
        """
        if self.is_empty():
            return 0
        count = 1
        tmp_cur = self._head
        while tmp_cur.next != self._head:
            count += 1
            tmp_cur = tmp_cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:无
        """
        if self.is_empty():
            return
        tmp_cur = self._head
        print(tmp_cur.item)
        while tmp_cur.next != self._head:
            tmp_cur = tmp_cur.next
            print(tmp_cur)

    def __add_first(self, node):
        """
        添加第一个元素
        :param node:
        :return:
        """
        if self.is_empty():
            self._head = node
            node.next = self._head
            return True
        return False


    def add(self, item):
        """
        头部添加节点
        :return:
        """
        is_result = True
        node = Node(item)

        if not self.__add_first(node):
            flag_node = self._head
            try:
                node.next = self._head
                tmp_cur = self._head
                while tmp_cur.next != self._head:
                    tmp_cur = tmp_cur.next
                tmp_cur.next = node
                self._head = node
            except Exception as e:
                print(e)
                # 回滚
                if flag_node != self._head:
                    tmp_cur.next = flag_node
                    self._head = flag_node
                is_result = False
        return is_result

    def append(self, item):
        """
        在尾部添加元素
        :param item: 需要加入的元素
        :return: 是否成功
        """
        is_result = True
        node = Node(item)
        if not self.__add_first(node):
            tmp_cur = self._head
            while tmp_cur.next != self._head:
                tmp_cur = tmp_cur.next
            tmp_cur.next = node
            node.next = self._head
        return is_result

    def insert(self, pos, item):
        """
        指定位置插入元素
        :param pos: 指定位置
        :param item: 元素
        :return: 是否成功
        """
        is_result = True
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            tmp_cur = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                tmp_cur = tmp_cur.next
            node.next = tmp_cur.next
            tmp_cur.next = node
        return is_result

    def remove(self, item):
        """
        删除一个节点
        :param item: 需要删除的节点
        :return:
        """
        is_result = True
        if self.is_empty():
            return False
        tmp_cur = self._head
        if tmp_cur.item == item:
            if tmp_cur.next != self._head:
                while tmp_cur.next != self._head:
                    tmp_cur = tmp_cur.next
                tmp_cur.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
            return is_result
        else:
            pre = self._head
            while tmp_cur.next != self._head:
                if tmp_cur.item == item:
                    pre.next = tmp_cur.next
                    return is_result
                else:
                    pre = tmp_cur
                    tmp_cur = tmp_cur.next
            if tmp_cur.item == item:
                pre.next = tmp_cur.next
                return is_result
        is_result = False
        return is_result

    def search(self, item):
        """
        查找节点是否存在
        :param item: 需要查找的元素
        :return: 是否存在
        """
        is_result = False
        if self.is_empty():
            return is_result
        tmp_cur = self._head
        if tmp_cur.item == item:
            is_result = True
            return is_result
        while tmp_cur.next != self._head:
            tmp_cur = tmp_cur.next
            if tmp_cur.item == item:
                is_result = True
                break
        return is_result



if __name__ == "__main__":
    ll = SignalCycLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()











