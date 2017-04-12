# _*_ coding: UTF-8 _*_

# python程序能用很多方式处理日期和时间，转换日期格式等功能

import time       # 引入时间模块
import calendar   # 引入日历模块

ticks = time.time()
print "当前时间为", ticks


ticks1 = time.localtime(time.time())
print "当前时间为：", ticks1


# python中提供了很多格式化时间格式的函数

#  格式化成2016-03-20  11：24：22形式
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


# python中还内置了可以直接获取某月份的日历
cal = calendar.month(2017, 4)
print "2017年4月份的日历如下："
print cal

# python中日期和时间模块中还有很多函数，后续学习中慢慢使用


