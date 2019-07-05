#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/5
@File     :   insert_sort
@note     :   插入排序
"""

def insert_sort(source_list):
    """
    插入排序
    :param source_list:
    :return:
    """
    for i in range(1, len(source_list)):
        for j in range(i, 0, -1):
            if source_list[j] < source_list[j - 1]:
                source_list[j], source_list[j - 1] = source_list[j - 1], source_list[j]


if __name__ == '__main__':
    tl = [23, 53, 1, 4, 20, 83, 12]
    print('before sort : ', tl)
    insert_sort(tl)
    print("after sort : ", tl)


