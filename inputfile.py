import sys
import pandas as pd
print("输入处理的文件名：")
input_file = sys.argv[1] 

chunks = pd.read_csv(input_file,  header=0, iterator = True,  engine='python')
chunk1 = chunks.get_chunk(1100) 
print(chunk1)
