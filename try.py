import pandas as pd
import os


def dataMerge(data_path, output_file, project):
    project = []
    # project_1032 = []

    for fileName in os.listdir(data_path):
        fileSplit = fileName.split('_')
        if fileSplit[0] == project:
            project.append(fileName)

    data = []
    for fileName in project:
        subPath = os.path.join(data_path, fileName)
        data = pd.read_csv(subPath)
        data.append(data)
    mergeData = pd.concat(data, axis=0)
    mergeData.to_csv(output_file)

    # data_1032 = []
    # for fileName in project_1032:
    #     subPath = os.path.join(data_path, fileName)
    #     data = pd.read_csv(subPath)
    #     data_1032.append(data)
    # mergeData_1032 = pd.concat(data_1032, axis=0)
    # mergeData_1032.to_csv(output_file_1032)

# if __name__ == "__main__":
#     months = ["01", "04", "07"]
#     for month in months:
#         data_path = f"./data/00_KSIOT_2021{month}"
#         output_file_756 = f"./output/{month}_756_merge.csv"
#         output_file_1032 = f"./output/{month}_1032_merge.csv"

#         dataMerge(data_path, output_file_756, "756")
#         dataMerge(data_path, output_file_756, "1032")



# groupby
dataMerges = pd.read_csv( r"./output/01_756_merge.csv")
# print(dataMerges)

# 建字典 結構從
unique_device_ids =list(dataMerges['DEVICE_ID'].unique())

#驗證是否拿到id
# print(7494382694 in unique_device_ids)
# print(7522863555 in unique_device_ids)
dataDict = {
    
}

for id in unique_device_ids:
    dataDict[id] = []





for index, row in dataMerges.iterrows():
    # print(row['c1'], row['c2'])
    # print(row['VOC(ppb)'])



    my_row = [
        row['DEVICE_ID'],
        row['LON'],
        row['LAT'],
        row['TIME'],
        row['PM2_5(μg/m3)'],
        row['PM10(mg/m3)'],
        row['TEMPERATURE(℃)'],
        row['HUMIDITY(%)'],
        row['WIND_SPEED(m/sec)'],
        row['VOC(ppb)'],
        row['WIND_DIRECT(degrees)']
    ]

    # 丟進字典
    dataDict[row['DEVICE_ID']].append(my_row)


# print(len(dataDict[7495890482])) 

# # # 不需使用的小垃圾
# # # groupBy = dataMerges.groupby(['DEVICE_ID'])
# # # print(groupBy)

# dataframe(array)
# 然後aggregate
# 


for key in dataDict:
    # dataDict[key]

    df = pd.DataFrame(dataDict[key], columns=['DEVICE_ID','LON', 'LAT', 'TIME', 'PM2_5(μg/m3)','PM10(mg/m3)',
                                                      'TEMPERATURE(℃)','HUMIDITY(%)','WIND_SPEED(m/sec)','VOC(ppb)','WIND_DIRECT(degrees)'])
    df.to_csv(f"{key}_01_756.csv")
