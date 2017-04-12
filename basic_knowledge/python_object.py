# _*_ coding: UTF-8 _*_

# 面向对象简介
"""
1、类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。
      对象是类的实例。
2、类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
3、数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
4、方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），
           也称为方法的重写。
5、实例变量：定义在方法中的变量，只作用与当前实例的类。
6、继承：即一个派生类继承基类的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样
        一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个"关系（Dog是一个Animal）。
7、实例化：创建一个类的实例，类的具体对象。
8、方法：类中定义的函数。
9、对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""
# 简单的python类实例
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, "Salary: ", self.salary

employee = Employee("sss", 234)
employee.displayCount()
employee.displayEmployee()

# python的内置属性
"""
1、__dict__:类的属性（包含一个字典，由类的数据属性组成）
2、__doc__:类的文档字符串
3、__name__:类名
4、__module__:类定义所在的模块（类全名是'__main__.className',如果类位于一个导入模块mymod中，
  那么calssName.__module__等于mymod)
5、__bases__:类的所有父类构成元素（包含类一个由所有父类组成的元组）
"""

# python的内置类属性调用实例
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__", Employee.__name__
print "Employee.__module__", Employee.__module__
print "Employee.__bases__", Employee.__bases__
print "Employee.__dict__", Employee.__dict__


# 析构函数__del__，在对象被销毁时调用
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)    # 打印对象id
del pt1
del pt2
del pt3

# 类的继承，通过继承实现代码重用
"""
1、在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中专门调用
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用函数时
   并不需要带上self参数。
3、python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。
  (首先在本类中查找调用方法，找不到才去基类中找）
4、如果在继承元组中列了一个以上的类，那么它就被称作"多重继承"
"""

#   继承实例

class Parent:         # 定义父类
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性：", Parent.parentAttr

class Child(Parent):    # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print "调用子类方法 child method"

c = Child()       # 实例化子类
c.childMethod()   # 调用子类方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)    # 再次调用父类方法
c.getAttr()       # 再次调用父类方法

# 方法重写
class Father:
    def myMethod(self):
        print "调用父类方法"

class Son(Father):
    def myMethod(self):
        print "调用子类方法"

s = Son()
s.myMethod()

# 类中的变量名前面加上__表示私有变量