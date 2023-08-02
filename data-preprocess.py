import pandas as pd
import os
import random



# merge 一大張
# shuffle打亂
# 按比例分配  6訊 2驗(一個腳本) # 2測(另一個腳本)

def reMerge(data_path, output_data):
    # projects = []

    # for fileName in os.listdir(data_path):
    #     fileSplit = fileName.split('_')
    #     if fileSplit[2] == project:
    #         projects.append(fileName)

    data = []
    for fileName in os.listdir(data_path):
        subPath = os.path.join(data_path, fileName)
        newdata = pd.read_csv(subPath)
        data.append(newdata)

    mergeData = pd.concat(data, axis=0)
    # noNull = mergeData.dropna(axis=1, how='any')
    # shuffled_data = mergeData.sample(frac=1)
    noNull.to_csv(output_data) 



if __name__ == "__main__":
    data_path = r"./agg15m"
    output_data = r"./forDL/raw_data.csv"
    reMerge(data_path, output_data)
   