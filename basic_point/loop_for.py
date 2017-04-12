# _*_ coding: UTF-8 _*_

# 普通for循环
for letter in 'Python':
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print '当前水果 :', fruit

print 'good bye'

# 通过序列索引迭代

for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

# 循环中使用else语句

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, ' 是一个质数'



