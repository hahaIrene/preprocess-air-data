import pandas as pd
import os


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
                                              'TEMPERATURE(℃)','HUMIDITY(%)','WIND_SPEED(m/sec)','VOC(ppb)',
                                              'WIND_DIRECT(degrees)'])
    df.to_csv(f"{key}_01_756.csv")
