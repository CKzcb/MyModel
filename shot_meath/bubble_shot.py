#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/4
@File     :   bubble_shot
@note     :   冒泡排序
"""

def bubble_sort(source_list):
    """
    冒泡排序
    :param source_list:需要排序的列表
    :return:排序后的列表
    """
    for i in range(len(source_list) - 1, 0, -1):
        for j in range(i):
            if source_list[j] > source_list[j + 1]:
                source_list[j], source_list[j + 1] = source_list[j + 1], source_list[j]


if __name__ == '__main__':
    tl = [54, 22, 45, 12, 9, 20, 89, 71]
    print("before sort : ", tl)
    bubble_sort(tl)
    print("after sort : ", tl)



