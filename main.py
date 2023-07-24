import pandas as pd
import os


jan_data_path = r"./data/00_KSIOT_202101"
apr_data_path = r"./data/00_KSIOT_202104"
july_data_path = r"./data/00_KSIOT_202107"

# os.listdir(jan_data_path)


# data = pd.read_csv(r"./756_107年高雄市空氣品質感測物聯網布建計畫_2021_01_0.csv")
# print(data)

#listdir 列出所有檔名 split分割字串  找檔名
project_756 = []
project_1032 = []
for fileName in os.listdir(jan_data_path):
    fileSplit = fileName.split('_')
    # print(fileSplit)
    

    if fileSplit[0] == "756":
        project_756.append(fileName)
    elif fileSplit[0] == "1032":
        project_1032.append(fileName)

# print(project_756)
# print(project_1032)


#把檔案的名稱join進路徑 然後加入陣列
data_756= []
for fileName in project_756:
    subPath = os.path.join(jan_data_path, fileName)
    data = pd.read_csv(subPath)
    data_756.append(data)
# print(data)

mergeData_756 = pd.concat(data_756,axis=0)
mergeData_756.to_csv(r'./output/jan_756_merge.csv')

# 然後要aggregate
# 試試把上面的東西def 

# def datamerge():
    