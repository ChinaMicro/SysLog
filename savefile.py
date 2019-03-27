# 只针对日志导出“警告”的记录，事先已经将记录按照“警告”筛选出来了。增加了选择“错误”类别。
# 用文本识别处理Windows 系统日志 - 2  2019.3.23
# 1. 先将日志样本用windows事件查看器打开，导出为csv或txt类文件，例中的文件名是20190305_sum_1.csv。
# 在CMD命令行中指定要读入的文件名，读入程序操作。
# 将日志记录按照列名“错误”和“警告”分类生成数组df_error和df_warn。
# 输出2个分类文件保存到d:\events\error\和 ..\warn\中
# 文件按照系统_类型_日期时间命名，以便于批命令自动操作。
# 查找步骤：
#读入日志文件，指定关键字，查找含有关键字的记录，按照关键字存储文件。
######################## makefile.py
import sys
# print("输入处理的文件名：") # 在命令行直接输入文件名：python savefile.py 20190305_sum_1.csv
input_file = sys.argv[1] 
import pandas as pd
# chunks = pd.read_csv('20190305_sum_1.csv',  header=0, iterator = True,  engine='python')
chunks = pd.read_csv(input_file,  header=0, iterator = True,  engine='python')
chunk1 = chunks.get_chunk(110000) # 分块赋值，否则内存不够。
# print(chunk1.columns) # Index(['级别', '日期和时间', '来源', '事件 ID', '任务类别', 'Unnamed: 5'], dtype='object')

# print(chunk1)
# df =pd.DataFrame(chunk1)
# print(df)

df = pd.DataFrame(chunk1)
df_error = df[df['级别'].isin(['错误'])]
df_warn = df[df['级别'].isin(['警告'])]
# print(df_error)
# print(df_warn)

# count = pd.DataFrame(pd.value_counts(chunk1['级别'].values,  sort=1)) # sort=1降序排列
# 所有级别发生次数的降序列表
# count  # 错误 501   警告 343
######################## savefile.py
# 存储文件 2019.3.26
import os
path_error = 'd:/events/error'
path_warn = 'd:/events/warn'
# 判断保存文件的目录是否存在，否则建立目录。
def exist(path):
    if os.path.exists(path) == False:
        if '.' not in path: # 如果路径名里面有".",就说明这个是文件名字，不是文件名就是目录名。
            os.makedirs(path)
            print(path + '  is made.')
# 按照不同的日志分类调用函数： 
exist(path_error)
exist(path_warn)

# 命名文件
import time
daytime = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
file = path_error +'/'+ "GuoWei_02_all_error"+daytime+".xls"
# 文件名字：国微_系统号_ 全部_错误日期时间.xls
df_error.to_excel(file, encoding="utf-8") # 保存为excel 文件
print(file + ' is sved.')
file = path_warn+'/'+ "GuoWei_02_all_warn"+daytime+".xls"
df_warn.to_excel(file, encoding="utf-8") # 保存为excel 文件
print(file + ' is sved.')

# 打开Excel表格观察添加注释后保存2种类型文件，xls和csc类。以便下一步继续统计。