Readme.txt 更新时间 2019. 4. 9.
SystemLog
系统日志管理

一，运行环境1.1 Python 3.4以上，本例使用3.6

1.2安装Anaconda。（http://continuum.io/downloads）其中包含的常用工具包： NumPy，Anaconda，Jupyter。

1.3 如果已经安装过的 Numpy 要求版本 1.11以上，本例使用1.14。

二，导出系统日志记录
用Windows事件查看器导出日志时按照详细，选项“错误”和“警告”可以勾选也可以不勾选，代码能够筛选出来，选项“WDI”和“经典”需要勾选，然后保存为CSV格式文件：日志文件.csv ，例如：'20190305_sum_1.csv'

三，再将CSV格式的日志文件读入程序操作。处理步骤：

读入日志文件，指定关键字，查找含有关键字的记录，按照关键字存储文件。代码中的筛选是根据日志中的列名'级别'指定'错误'和'警告'选择记录。代码如下： df_error = df [df ['级别'] .isin（['错误']）]和df_warn = df [df ['级别'] .isin（['警告']）]

将按照'错误'和'警告'分类的记录文件分别保存在以下指定的目录中：path_error ='d：/ events / error'和path_warn ='d：/ events / warn'

四，保存的文件按照系统_类型_日期生成时间命名，以便于批命令自动操作.d：/events/error/GuoWei_02_all_error20190326-225343.xls和d：/events/warn/GuoWei_02_all_warn20190326-225343.xls

五，以上的代码中的字符可以根据需要对应改动。

六，执行代码

1. 将导出的日志文件保存到程序所在的目录中，如：c:\users\user\syslog\。

2. 运行程序的方式：

	2.1 批命令自动执行方式：
	程序名：syslog-CMD.py 
        进入Windows的命令行cmd模式，
	在Python的Anaconda默认目录下执行主程序c:\users\user\syslog\>python syslog-CMD.py 日志文件.csv。

	2.2 用Jupyter Notebook手动执行方式： 
        程序名：syslog-Jupyter.py
	先用NotePad 打开syslog-Jupyter.py文件，将全部代码复制，
	再进入Jupyter Notebook中，新建一个Floder，命名为syslog，
	在syslog的Folder中新建一个Python 3的Cell , 将复制的syslog-Jupyter.py代码粘贴进去。
	直接Run。

七，查看经过处理的日志文件
	
	经过处理的日志文件默认存放在d:\events\error\和d:\events\warn中，如果清空目录再执行程序可以自动重建。
