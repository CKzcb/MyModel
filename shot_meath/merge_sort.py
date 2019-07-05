#!/usr/bin/python3
"""
@Author   :   zhuchb
@time     :   2019/7/5
@File     :   merge_sort
@note     :   归并排序
"""

def merge_sort(source_list):
    """
    归并排序
    :param source_list:
    :return:
    """
    if len(source_list) <= 1:
        return source_list
    # 二分法
    num = len(source_list) // 2
    left = merge_sort(source_list[:num])
    right = merge_sort(source_list[num:])
    # 合并
    return merge(left, right)

def merge(left, right):
    """
    合并操作
    :param left:
    :param right:
    :return:
    """
    print("left : ", left)
    print("righ : ", right)
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    print(result)
    return result

if __name__ == '__main__':
    tl = [2, 53, 12, 94, 22, 32, 19]
    print("before sort : ", tl)
    tl = merge_sort(tl)
    print("after sort : ", tl)
