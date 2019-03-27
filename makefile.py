# 只针对日志导出“警告”的记录，事先已经将记录按照“警告”筛选出来了。增加了选择“错误”类别。
# 用文本识别处理Windows 系统日志 - 2  2019.3.23
# 1. 先将日志样本用windows事件查看器打开，导出为csv或txt类文件，
# 再读入程序操作
# 查找步骤：
#读入日志文件，指定关键字，查找含有关键字的记录，按照关键字存储文件。

import pandas as pd
chunks = pd.read_csv('20190305_sum_1.csv',  header=0, iterator = True,  engine='python')
chunk1 = chunks.get_chunk(110000) # 分块赋值，否则内存不够。
print(chunk1.columns) # Index(['级别', '日期和时间', '来源', '事件 ID', '任务类别', 'Unnamed: 5'], dtype='object')

# print(chunk1)
# df =pd.DataFrame(chunk1)
# print(df)

df = pd.DataFrame(chunk1)
df_error = df[df['级别'].isin(['错误'])]
df_warn = df[df['级别'].isin(['警告'])]
print(df_error)
print(df_warn)

count = pd.DataFrame(pd.value_counts(chunk1['级别'].values,  sort=1)) # sort=1降序排列
# 所有级别降序列表
# count  # 错误 501   警告 343

# 存储文件
print('making file ...')
df_error.to_excel("GuoWei_02_sum_error.xls", encoding="utf-8") # 保存为excel 文件
df_warn.to_excel("GuoWei_02_sum_warn.xls", encoding="utf-8")
print('make over')
# 打开Excel表格观察添加注释后保存2种类型文件，xls和csc类。以便下一步继续统计。