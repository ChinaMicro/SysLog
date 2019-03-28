# SystemLog
系统日志管理

一、运行环境
1.1 Python 3.4以上，本例使用3.6
1.2 安装Anaconda。（http://continuum.io/downloads）其中包含的常用工具包：
    NumPy的，Anaconda，Jupyter。
1.3 Numpy 1.11以上，本例使用1.14 

二、导出系统日志记录  
    用Windows事件查看器导出日志时按照详细，选项“错误”和“警告”可以勾选也可以不勾选，代码能够筛选出来，
选项“WDI”和“经典”需要勾选，然后保存为CSV格式文件。例：
'20190305_sum_1.csv'
'20190305_sum_1.csv'
只是未经代码处理的Excel表格的显示内容里面有分行符，内容多的行过高。可能是 \t。

三、再将CSV格式的日志文件读入程序操作。
    处理步骤：
1.  读入日志文件，指定关键字，查找含有关键字的记录，按照关键字存储文件。
代码中的筛选是根据日志中的列名‘级别’指定‘错误’和‘警告’选择记录。代码如下：
df_error = df[df['级别'].isin(['错误'])]
df_warn = df[df['级别'].isin(['警告'])]

2.  将按照‘错误’和‘警告’分类的记录文件分别保存在以下指定的目录中：
path_error = 'd:/events/error'
path_warn = 'd:/events/warn'

四、保存的文件按照系统_类型_日期生成时间命名，以便于批命令自动操作。
d:/events/error/GuoWei_02_all_error20190326-225343.xls
d:/events/warn/GuoWei_02_all_warn20190326-225343.xls

五、 以上的代码中的字符可以根据需要对应改动。

六、执行代码
   进入Windows的命令行cmd模式，在Python的Anaconda默认目录下执行主程序    c：\ users \ user> python savefile.py日志文件.csv  
    
七，增加主程序版本
    savefile_main.py 作为在命令行执行的代码，增加了输入日志文件是否可读的判断，如果不可读给出提示信息。
