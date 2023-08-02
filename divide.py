import pandas as pd
import numpy as np

# 讀取原始資料
data = pd.read_csv(r"./forDL/shuffled_data.csv")

# 計算資料分配的數量
total_records = len(data)
file1 = int(0.6 * total_records)
file2 = int(0.2 * total_records)
file3 = total_records - file1 - file2


# 分配資料到不同的檔案
file1_data = data.iloc[:file1, :]
file2_data = data.iloc[file1:file1+file2, :]
file3_data = data.iloc[file1+file2:, :]

# 將資料寫入檔案
file1_data.to_csv('training.csv', index=False)
file2_data.to_csv('testing.csv', index=False)
file3_data.to_csv('validation.csv', index=False)
