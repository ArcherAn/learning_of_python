# _*_ coding: UTF-8 _*_

list1 = ['physics', 'chemistry', 1997, 2001]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

#   访问列表中的值与访问字符串中某一位置的值相同

print list1[0]
print list2[1:5]        # 打印的依然是列表   [2, 3, 4, 5]


#  列表可以更新  下一节中的元组无法更新

list1[2] = 2000
print list1

# 还可以通过append()函数进行更新

list1.append(2003)
print list1

"""
# python 列表中的不分函数
cmp(list1, list2)        # 比较两个列表的元素
len(list)                # 列表元素个数
max(list)                # 返回列表元素最大值
min(list)                # 返回列表元素中最小值
list(seq)                # 将元组转换为列表
"""

"""
# python中包含的方法
list.append(obj)         # 在列表末尾添加新的对象
list.count(obj)          # 统计某个元素在列表中出现的次数
list.extend(seq)         # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原列表）
list.index(obj)          # 从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)  # 将对象插入列表
list.pop(obj=list[-1])   # 移除列表中的一个元素（默认最后一个），并且返回该元素的值
list.remove(obj)         # 移除列表中某个值的第一个匹配项
list.reverse()           # 反向列表中的元素
list.sort([func])        # 对原列表进行排序
"""