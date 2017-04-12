# _*_ coding: UTF-8 _*_
import math

# 一个py结尾的python文件就是一个模块，包含python定义和python语句

# from...import语句 让从模块中导入一个指定的部门到当前命名空间
# 例如要导入模块 fib 的 fibonacci 函数，使用语句如下：
# from fib import fibonacci

# from...import * 语句 表示导入模块中全部内容

# from math import *

content = dir(math)
print content
