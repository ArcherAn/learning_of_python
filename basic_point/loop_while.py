# _*_ coding: UTF-8 _*_
# while循环语句

count = 0
while count < 9:
    print 'The count is:', count
    count = count + 1

print "good bye"

# continue 和 break 的用法

# contine 只是跳出此次循环不执行  break 是跳出整个循环，后续的循环都不执行
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i

j = 1
while 1:
    print j
    j += 1
    if j > 10:
        break


# 循环语句中使用 else 语句
num = 0
while num < 5:
    print num, "is less than 5"
    num = num + 1
else:
    print num, "is not less than 5"




