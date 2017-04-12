# _*_ coding: UTF-8 _*_

#  输出 2～100之间所有的素数

i = 2
while i < 100:
    j = 2
    while j <= (i/j):
        if not (i % j):
            break
        j += 1
    if(j > i/j):
        print i, ' 是素数'
    i += 1
print "good bye!"
