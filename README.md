# Sdbys_Scrapy
A Scrapy spider for www.sdbys.cn.
Just for exercising.
### 参考文章
卧槽哥的Scrapy教程 http://cuiqingcai.com/3472.html
### 版本信息
PyCharm Community Edition 2017.2.3

```
C:\Users\long>conda -V
conda 4.3.30

C:\Users\long>python -V
Python 3.6.2 :: Anaconda, Inc.

C:\Users\long>conda list Scrapy
# packages in environment at C:\ProgramData\Anaconda3:
#
scrapy                    1.4.0            py36h764da0a_1

C:\Users\long>conda list BeautifulSoup
# packages in environment at C:\ProgramData\Anaconda3:
#
beautifulsoup4            4.6.0            py36hd4cc5e8_1
```
### 准备工作
- 安装Scrapy

在cmd中执行：``` conda install Scrapy``` 没权限请用管理员
- 安装一个Python操作MySQL的包，来自MySQL官方的一个包：[点我下载](http://cos.zerlong.com/mysql-connector-python-2.1.7.zip)

下载完成后解压出来，从CMD进入该目录的绝对路径，然后 Python setup.py install ；即可完成安装
### 数据库信息
MySQL 5.5.4
```
user='root', password='root', host='127.0.0.1', database='sdbys'
```
表结构
```
-- ----------------------------
-- Table structure for sdbys_tb1
-- ----------------------------
DROP TABLE IF EXISTS `sdbys_tb1`;
CREATE TABLE `sdbys_tb1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `degree` varchar(40) DEFAULT NULL,
  `specialty` varchar(100) DEFAULT NULL,
  `graduation` int(11) DEFAULT NULL,
  `school` varchar(100) DEFAULT NULL,
  `posttime` datetime DEFAULT NULL,
  `guid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `guid_uq` (`guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
### How to start
 请修改 sdbys/spiders/sdbys.py 第16行 为开始与结束页数
 
 运行entrypoint.py开使爬取
 
  ![image](https://github.com/rilego/sdbys_scrapy/blob/master/sdbys/20171206171328.png?raw=true)