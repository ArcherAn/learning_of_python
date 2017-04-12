# _*_ coding: UTF-8 _*_

# 定义函数：
"""
1、函数代码块以 def 关键词开头，后接函数标识浮名称和圆括号()
2、任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
3、函数的第一行语句可以选择性得使用文档字符串--用于存放函数说明
4、函数内容以冒号起始，并且缩进
5、return[表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None
"""

#  函数示例
#  实现一个函数，将一个字符串作为传入参数，再打印出来
def printme( str ):
    print str
    return

printme("调用用户自定义函数")

# python中，strings,tuples,numbers均是不可更改对象，而list,dict为可修改的对象

# python传不可变对象实例
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print b     # 结果是 2

# python传可变对象实例
def changeme( mylist ):
    mylist.append([1, 2, 3, 4])
    print "函数内取值：", mylist
    return

# 调用 changme 函数
mylist = [10, 20, 30]
changeme(mylist)
print "函数外取值：", mylist

# 函数返回值
total = 0
def sum( arg1, arg2 ):
    total = arg1 + arg2
    print "函数内 : ", total
    return total
total1 = sum( 10, 20 )
print total      # 局部变量和全局变量的关系
print total1



