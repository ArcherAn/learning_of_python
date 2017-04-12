# _*_ coding: UTF-8 _*_

#  字典是另一种可变容器模型，且可存储任意类型对象。
#  字典中的每个键值对用：进行分割，每个对之间用，分割，字典放置于{}中，格式如下：
#  d={key1 : value1, key2: value2 }    键必须是唯一的

dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

print dict1['Alice']


#  字典可以修改

dict1['Alice'] = '2221'
print dict1

# 字典中的元素可以单独修改，也可以整个清除
del dict1['Alice']      # 删除单个条目
dict1.clear()           # 清空字典中所有条目
del dict1               # 删除字典


#  字典中的内置函数
"""
cmp(dict1, dict2)       # 比较两个字典中的元素
len(dict)               # 计算字典元素个数，既键的总数。
str(dict)               # 输出字典可打印的字符串表示。
type(variable)          # 返回输入的变量类型，如果变量是字典就返回字典类型
"""

#  字典中的内置方法
"""
dict.clear()            # 删除字典内所有元素
dict.copy()             # 返回一个字典的浅复制
dict.keys()             # 以列表返回一个字典中所有的键
dict.items()            # 以列表返回可遍历的元组数组
dict.values()           # 以列表返回字典中的所有值
"""

