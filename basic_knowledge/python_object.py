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

