# -*- coding: utf-8 -*-
类是一组用来描述如何生成一个对象的代码段

一.类对象
创建类对象
class ObjectCreator(object):
    pass
python中的类，本质上仍然是一个对象，可以实现如下操作
1. 可以将它赋值给一个变量
ObjectCreatorMirror = ObjectCreator
print ObjectCreatorMirror
2. 可以拷贝它
3. 可以为它增加属性
ObjectCreator.new_attribute = 'foo'
#打印布尔值，判断ObjectCreator对象是否有属性'new_attribute'
print hasattr(ObjectCreator,'new_attribute')
4. 可以将它作为函数参数进行传递
def echo(o):
    print o
echo(objectCreator)

二.动态地创建类
可以在运行时动态的创建它们
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('foo')
#打印类，不是类的实例
print MyClass
#类的类型是type?
print isinstance(MyClass,type)
#常见类实例
print MyClass()
print type(MyClass())

三.使用type创建类
type(类名，父类名称组成的元组，包含属性的字典)
#定义了Test2类
Test2 = type("Test2",(),{})
#打印Test2类的实例对象
print Test2()

四.使用type创建带有方法的类
def echo_bar(self):
    print self.bar
Foo = type('Foo',(),{'echo_bar':echo_bar})

五.元类
元类就是创建类对象的，元类就是类的类，类似于泛函与函数的关系
#使用元类创建出一个对象，这个对象称为类
MyClass = MetaClass()
#使用MyClass这个“类”来创建实例对象
MyObject = MyClass()
#type就是一个元类，可以创建类对象

六.__metaclass__属性
class Foo(object):
    __metaclass__ = something (act as type)
Python做了如下的操作：
Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。


