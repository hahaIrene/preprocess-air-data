import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# scikit-learn 套件

# 讀取原始資料
data = pd.read_csv(r"./data/shuffled_data.csv")

def standardizeDataFrame(sdData, columns):
    # sdData[columns] = StandardScaler().fit_transform(sdData[columns])
    scaler = MinMaxScaler(feature_range=(-1, 1))
    sdData[columns] = scaler.fit_transform(sdData[columns])
    return sdData

data = standardizeDataFrame(data, ['PM2_5(μg/m3)' ,'TEMPERATURE(℃)' 
                                   ,'HUMIDITY(%)' , 'VOC(ppb)'])

data.to_csv(r'./data/for_chart_sd.csv')
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
file1_data.to_csv(r'./data/training.csv', index=False)
file2_data.to_csv(r'./data/testing.csv', index=False)
file3_data.to_csv(r'./data/validation.csv', index=False)


