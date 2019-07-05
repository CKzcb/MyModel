#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/4
@File     :   selection_sort
@note     :   选择排序
"""

def selection_sort(source_list):
    """
    选择排序
    :param source_list:
    :return:
    """
    l_len = len(source_list) - 1
    for i in range(l_len):
        min_index = i
        for j in range(i + 1, l_len):
            if source_list[j] < source_list[min_index]:
                min_index = j
        if min_index != i:
            source_list[i], source_list[min_index] = source_list[min_index], source_list[i]


if __name__ == '__main__':
    tl = [43, 21, 4, 98, 25, 17, 65]
    print("before sort : ", tl)
    selection_sort(tl)
    print("after sort : ", tl)
