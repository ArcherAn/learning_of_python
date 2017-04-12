# _*_ coding: UTF-8 _*_

# python  字符串
var1 = 'hello python'
print (var1[1])
print (var1[0:2])
print (var1[0:9:3])    # 最后面的3表示步长

#  更新字符串
print '更新后的字符串' , var1[:6] + 'world'

# 字符串格式化

print "my name is %s and age is %d" % ('anan', 23)

'''
%c     格式化字符及其ascii码
%s     格式化字符串
%d     格式化整数
%o     格式化无符号八进制数
%x     格式化十六进制数
'''


