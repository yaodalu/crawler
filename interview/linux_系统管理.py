# -*- coding: utf-8 -*-
#Linux命令-系统管理
cal         查看当前日历

date        显示或设置时间(需要管理员权限)
eg:
    %Y %m %d %H %M %S
    date '+%Y/%m/%d'

ps          查看进程信息
eg:
    1. ps -r
    只显示正在运行的进程
    2. ps -a
    显示终端上的所有进程，包括其他用户的进程

kill        终止进程
eg:
    kill [-signal] pid
    signal从0-15,9为绝对终止

init0           关机
init6           重启
reboot          重新启动操作系统
shutdown -h time在某个time时刻关系

df              检测磁盘空间,-m表示1024byte显示
du              检测目录或文件的磁盘空间
eg:
    du [options] 目录/文件名


ifconfig        查看网卡信息

ping            测试远程主机连通性
eg:
    ping 域名/IP
