import pandas as pd
import numpy as np
import os



# # groupby
# dataMerges = pd.read_csv( r"./output/01_756_merge.csv")
# # print(dataMerges)

# # 建字典 結構抓id再強制轉list
# unique_device_ids =list(dataMerges['DEVICE_ID'].unique())

# #驗證是否拿到id
# # print(7494382694 in unique_device_ids)
# # print(7522863555 in unique_device_ids)
# dataDict = {
    
# }

# for id in unique_device_ids:
#     dataDict[id] = []



# for index, row in dataMerges.iterrows():
#     # print(row['c1'], row['c2'])
#     # print(row['VOC(ppb)'])


#     my_row = [
#         row['DEVICE_ID'],
#         row['LON'],
#         row['LAT'],
#         row['TIME'],
#         row['PM2_5(μg/m3)'],
#         row['PM10(mg/m3)'],
#         row['TEMPERATURE(℃)'],
#         row['HUMIDITY(%)'],
#         row['WIND_SPEED(m/sec)'],
#         row['VOC(ppb)'],
#         row['WIND_DIRECT(degrees)']
#     ]

#     # 丟進字典
#     dataDict[row['DEVICE_ID']].append(my_row)


# print(len(dataDict[7495890482])) 

# # # 不需使用的小垃圾
# # # groupBy = dataMerges.groupby(['DEVICE_ID'])
# # # print(groupBy)

# # dataframe(array)
# # 然後aggregate


# # 叫出符合KEY的字典組DATAFRAME 要從python 本身的陣列格式轉成nmpy array
# for key in dataDict:
#     # dataDict[key]

#     df = pd.DataFrame(dataDict[key], columns=['DEVICE_ID','LON', 'LAT', 'TIME', 'PM2_5(μg/m3)','PM10(mg/m3)',
#                                               'TEMPERATURE(℃)','HUMIDITY(%)','WIND_SPEED(m/sec)','VOC(ppb)',
#                                               'WIND_DIRECT(degrees)'])
#     df.to_csv(f"{key}_01_756.csv")





def deviceGroup (month, project):
    if os.path.exists(r'./device') == False:
        os.makedirs(r'./device')

    output_path = f'./device/{project}-{month}'
    if os.path.exists(output_path) == False:
        os.makedirs(output_path)
    
    dataMerges = pd.read_csv(f"./output/{month}_{project}_merge.csv")
    unique_device_ids =list(dataMerges['DEVICE_ID'].unique())
    dataDict = {
    
    }
    for id in unique_device_ids:
        dataDict[id] = []



    for index, row in dataMerges.iterrows():
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

    
    dataDict[row['DEVICE_ID']].append(my_row)


    # Dictionary = {
    #     "DeviceA": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     "DeviceB": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     "DeviceC": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     "DeviceD": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    # }
    # np.array(Dictionary["DeviceA"])

    for key in dataDict:
        # dataDict[key]

        try:
        df = pd.DataFrame(np.array(dataDict[key]), columns=['DEVICE_ID','LON', 'LAT', 'TIME', 'PM2_5(μg/m3)','PM10(mg/m3)',
                                                'TEMPERATURE(℃)','HUMIDITY(%)','WIND_SPEED(m/sec)','VOC(ppb)',
                                                'WIND_DIRECT(degrees)'])
        
        filepath = os.path.join(output_path, f"{key}_{month}_{project}.csv")
        df.to_csv(filepath)
        except:




deviceGroup("01","756")
deviceGroup("04","756")
deviceGroup("07","756")

deviceGroup("01","1032")
deviceGroup("04","1032")
deviceGroup("07","1032")