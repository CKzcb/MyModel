#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/5
@File     :   quick_sort
@note     :   快速排序
"""

def quicke_sort(source_list, start, end):
    """
    快速排序
    :param source_list:需要排序的队列
    :param start: 开始下标
    :param end: 结束下标
    :return:
    """
    # 退出条件
    if  start >= end:
        return
    # 设置其实元素为要寻找位置的基准元素
    mid = source_list[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and source_list[high] > mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        source_list[low] = source_list[high]

        # 如果low与high为重合，low指向的元素比基准元素小，则low向右移动
        while low < high and source_list[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        source_list[high] = source_list[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置上
    source_list[low] = mid

    # 基准元素左边的子序列进行快速排序
    quicke_sort(source_list, start, low - 1)

    # 基准元素右边的子序列进行快速排序
    quicke_sort(source_list, low + 1, end)


if __name__ == '__main__':
    tl = [2, 53, 12, 94, 22, 32, 19]
    print("before sort : ", tl)
    quicke_sort(tl, 0, len(tl) - 1)
    print("after sort : ", tl)





