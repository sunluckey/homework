## git作业

第一题：git add和git stage的区别是什么。

add的作用是将要提交的作业加到暂存区，stage就是暂存区的意思，两者区别不大。

第二题：git rm --cached 和git rm -f的区别是什么。

rm -- cached是留着你工作目录中不想删除的文件，而rm -f是强制删除文件。

第三题：git和svn的区别是什么。

git把内容按照元数据方式储存，svn是按照文件储存。

git是分布式，svn不是。

git可以有无限个版本库，svn只能有一个指定中央版本库。

git每个人可以在自己的本地库开放无限个分支，而svn分支是一个完整的目录，且这个目录拥有完整的实际文件。

git没有一个全局版本号，svn有。

第四题：筛选出 2018.10.1到2018.10.20之间的日志,并且输出为地理图,并且没有做过合并。

![avatar](https://github.com/sunluckey/homework/blob/homework/gitwork/%E7%AC%AC%E5%9B%9B%E9%A2%98.png?raw=true)

第五题：git init和git clone的区别？

git init是将一个目录初始化为git仓库，在你想变成git仓库的目录中执行该命令，执行后改目录中会有一个.git的子目录，这个就是仓库；git clone是克隆一个git仓库。

第六题：每次提交都忽略.idea文件夹里面的东西怎么办？

![avatar](https://github.com/sunluckey/homework/blob/homework/gitwork/%E7%AC%AC%E5%85%AD%E9%A2%98.png?raw=true)

第七题：如果编辑一个文件之后并且加入了暂存区,但是你后悔了,想把文件恢复到没有修改之前的样子,怎么办。

可以使用git reset HEAD <文件名>命令恢复。

第八题：如何检出标签?

先使用git tag 添加标签名，然后再用git show 标签名查看就行了。

第九题：git fetch 和 git pull的区别？

都是从远程仓库获取最新版本到本地，但是fetch不会自动merge，pull会。

第十题：如何添加远程仓库？

使用git remote add  name url命令添加远程仓库。