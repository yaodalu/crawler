# -*- coding: utf-8 -*-
pdb是基于命令行的调试工具

命令              简写命令        作用
break             b             设置断点
continue          c             继续执行程序
list              l             查看当前行的代码段
step              s             进入函数
return            r             执行代码直到从当前函数返回
quit              q             中止并退出
next              n             执行下一行
print             p             打印变量的值
help              h             帮助
args              a             查看传入参数
                  回车           重复上一条指令
break lineno      b lineno      在指定行设置断点
clear num                       删除指定断点
bt                              查看函数调用栈帧？

#当程序执行到pdb.set_trace()时位置调试
pdb.set_trace()
