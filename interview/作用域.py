# -*- coding: utf-8 -*-
Python使用LEGB规则来寻找一个符号对应的对象
locals - > enclosing function -> globals -> builtins
locals      当前所在命名空间(如函数、模块),函数的参数也属于命名空间内的变量
enclosing   外部嵌套函数的命名空间(闭包)
globals     全局变量，函数定义所在模块的命名空间
builtins    内建模块的命名空间

python在启动时会自动载入内建的函数，类
可以使用dir(__builtin__)查看
