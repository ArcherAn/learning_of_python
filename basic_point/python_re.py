# _*_ coding: UTF-8 _*_
import re

# python正则表达式方便检查一个字符串是否与某种模式匹配
"""
re.match(pattern, string, flags)
1、pattern: 匹配的正则表达式
2、string: 要匹配的字符串
3、flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
"""
# 实例
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print "matchObj.group(): ", matchObj.group()
    print "matchObj.group(1): ", matchObj.group(1)
    print "matchObj.group(2): ", matchObj.group(2)
else:
    print "No Match"
