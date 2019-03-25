# -*- coding: utf-8 -*-
#linux基本命令

ls           当前目录所有文件
ls --help 
man ls       查找manual
tab          自动补全
clear        清屏
cd           切换到主目录
cd.          切换到当前目录
/            根路径需要加
pwd          显示当前路径

mkdir        创建目录 a/b/c -p递归创建目录
tree         以目录树的方式显示
rmdir        删除目录
rm           删除文件

ln           硬链接，只能链接普通文件，不能链接目录，占用相同的空间
ln -s        软链接，不占磁盘空间，源文件删除则软链接失效
eg:
    ln -s 源文件 链接文件


>            输出重定向，将显示在终端上的内容保存到指定文件中
cat          查看文件内容
eg:
    ls > 重定向文件

cp           复制文件

tar          打包文件
eg：
    tar -cvf xxx.tar
    tar -zcvf xxx.tar.gz 打包压缩
gzip         压缩解压
gzip -d      解压
gzip -r      压缩

