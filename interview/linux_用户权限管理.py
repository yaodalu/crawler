# -*- coding: utf-8 -*-
#linux 命令-用户、权限管理
whoami          查看当前用户
who             查看当前所有登录系统的用户信息
exit            退出登录账户

useradd         添加用户账户,每个用户都要有一个主目录，默认/home/用户
eg:
    useradd abc -m -d /home/abc 
    创建abc用户，指定用户登录系统时的主目录为/home/abc，没有就自动建立，用户组默认是abc

    useradd a  -m -d /home/a -g test
    创建a用户，指定用户登录系统的主目录是/home/a，没有就自动建立，指定组名test

passwd          用户可以直接使用该命令修改自己的口令，后面无需加用户名
eg:
    sudo passwd 用户名
    超级用户可以使用passwd为普通用户修改口令

userdel         删除用户名
eg:
    userdel abc
    删除用户名，不删除主用户目录
    userdel -r abc
    删除用户名和主目录

su              切换用户
eg:
    su 用户名
    切换用户，不切换主目录
    su - 用户名
    切换用户，切换主目录名

cat /etc/group  查看有哪些用户组

groupadd        添加组账户
groupdel        删除组用户
usermod         修改用户所在组
eg:
    usermod -g 用户组 用户名
    usermod -a -G XXX 用户名
    向用户组XXX中添加用户

eg:
    为创建的普通用户添加sudo权限？
    1. sudo usermod -a -G adm 用户名
    超级用户向用户组adm中添加新创建的用户
    2. sudo usermod -a -G sudo 用户名
    超级用户将普通用户添加到sudo用户组中

chmod           修改文件权限
eg:
    chmod u/g/o/a/+/-/=/r/w/x/ 用户名
    1. u
    user表示该文件的所有者
    2. g
    group表示所有者同组用户
    3. o
    表示其他以外的人
    4. a
    1-3三者皆是
    5. +/-/=
    增加权限/撤销权限/设定权限
    6. r/w/x
    读取/写入/cd

chown           修改文件所有者
eg:
    chown 用户名 文件名

chgrp           修改文件所属组

