#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/5
@File     :   shell_sort
@note     :   希尔排序
"""

def shell_sort(source_list):
    """
    希尔排序
    :param source_list:
    :return:
    """
    nlen = len(source_list)
    # 初始步长
    gap = nlen // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, nlen):
            j = i
            # 插入排序
            while j >= gap and source_list[j - gap] > source_list[j]:
                source_list[j - gap], source_list[j] = source_list[j], source_list[j - gap]
                j -= gap
        gap = gap // 2



if __name__ == '__main__':
    tl = [2, 53, 12, 94, 22, 32, 19]
    print("before sort : ", tl)
    shell_sort(tl)
    print("after sort : ", tl)
