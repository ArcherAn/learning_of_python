# _*_ coding: UTF-8 _*_

# python 中提供了很多内置的输入输出函数，其中最简单的是print

# 读取键盘输入的函数
# raw_input  input

str = raw_input("请输入：")
print "你输入的内容是：", str

# input 函数不同的是可以接收一个python表达式作为输入，并将运算结果返回

str = input("请输入：")   # 输入内容为：[x*5 for x in range(2,10,2)]
print "你输出的内容是：", str


# 打开和关闭文件
# file object = open(file_name [, accsee_mode][, buffering])


