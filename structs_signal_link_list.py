#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/6/17
@File     :   structs_signal_link_list
@note     :   单向链表
"""

class SingleNode:
    """单个节点类"""
    def __init__(self, item):
        """
        :param item:数据元素
               next:下一节点
        """
        super(SingleNode, self).__init__()
        self.item = item
        self.next = None


class SingleLinkList:
    """单向链表类"""
    def __init__(self):
        super(SingleLinkList, self).__init__()
        self._head = None

    def is_empty(self):
        """
        链表是否为空
        :return: True or False
        """
        return self._head == None

    def length(self):
        """
        链表长度
        :return: count : 链表的长度
        """
        tmp_cur_node = self._head
        count = 0
        while tmp_cur_node != None:
            count += 1
            tmp_cur_node = tmp_cur_node.next
        return count

    def travel(self):
        """
        遍历链表
        :return: 无
        """
        tmp_cur_node = self._head
        while tmp_cur_node != None:
            print(tmp_cur_node.item)
            tmp_cur_node = tmp_cur_node.next

    def add(self, item):
        """
        头部添加元素
        :param item:需要添加的元素
        :return: 是否成功，失败会进行回滚
        """
        is_result = True
        tmp_head = self._head
        try:
            tmp_node = SingleNode(item)
            tmp_node.next = self._head
            self._head = tmp_node
        except Exception as e:
            print(e)
            self._head = tmp_head
            is_result = False
        finally:
            return is_result

    def append(self, item):
        """
        尾部添加元素
        :param item:需要添加的元素
        :return: is_result : 是否成功，失败会回滚
        """
        is_result = True
        last_node = None
        try:
            tmp_node = SingleNode(item)
            if self.is_empty():
                self._head = tmp_node
            else:
                tmp_cur = self._head
                last_node = tmp_cur
                while tmp_cur.next != None:
                    tmp_cur = tmp_cur.next
                    last_node = tmp_cur
                tmp_cur.next = tmp_node
        except Exception as e:
            print(e)
            # 进行回滚
            if (last_node != None) and tmp_cur != last_node:
                last_node.next = None
            elif last_node == None:
                self._head = None
            is_result = False
        finally:
            return is_result

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos: 指定位置
        :param item: 需要添加的元素
        :return: is_result : 是否成功
        """
        is_result = True
        if pos < 0:
            is_result = self.add(item)
        elif pos > (self.length() - 1):
            is_result = self.append(item)
        else:
            pre_node = self._head
            flag_node = pre_node.next
            count = 0
            try:
                tmp_node = SingleNode(item)
                while count < (pos - 1):
                    count += 1
                    pre_node = pre_node.next
                    flag_node = pre_node.next
                tmp_node.next = pre_node.next
                pre_node.next = tmp_node
            except Exception as e:
                print(e)
                if pre_node.next != flag_node:
                    pre_node.next = flag_node
                is_result = False
        return is_result

    def remove(self, item):
        """
        删除指定元素
        :param item:需要删除的元素
        :return: is_result : 返回是否成功
        """
        is_result = True
        tmp_cur = self._head
        tmp_pre = None
        while tmp_cur != None:
            if tmp_cur.item == item:
                if not tmp_pre:
                    self._head = tmp_cur.next
                else:
                    tmp_pre.next = tmp_cur.next
                break
            else:
                tmp_pre = tmp_cur
                tmp_cur = tmp_cur.next
        else:
            is_result = False
        return is_result

    def search(self, item):
        """
        查找节点是否存在
        :param item: 需要查找的元素
        :return: 返回是否存在True:False
        """
        is_result = False
        tmp_cur = self._head
        while tmp_cur != None:
            if tmp_cur.item == item:
                is_result = True
                break
            else:
                tmp_cur = tmp_cur.next
        return is_result




if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:", ll.length())

    ll.travel()
    print(ll.search(3))

    print(ll.search(5))

    ll.remove(1)
    print("length:", ll.length())

    ll.travel()
