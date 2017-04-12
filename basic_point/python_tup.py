# _*_ coding: UTF-8 _*_

#  元组与列表类似，但是无法修改
tup1 = ('physics', 'chemistry', 1997, 2001)
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a', 'b', 'c', 'd', 'e'

print tup1
print tup2
print tup3


# 元组中的元素值不允许删除，但可以使用del语句对整个元组进行删除

del tup1

"""
# 元组的内置函数
cmp(tuple1, tuple2)       # 比较两个元组的元素
len(tuple)                # 列表元组个数
max(tuple)                # 返回元组元素最大值
min(tuple)                # 返回元组元素中最小值
tuple(seq)                # 将列表转换为元组
"""