import pandas as pd
import os

# # 使用resample方法，指定"timestamp"欄位為時間索引，並將資料aggregate成15分鐘一筆，取資料的平均值（或其他適當的統計指標）
# df_aggregated = df.resample("15T", on="timestamp").mean()



# 欄位們
# my_row = [
        #     row['DEVICE_ID'],
        #     row['LON'],
        #     row['LAT'],
        #     row['TIME'],
        #     row['PM2_5(μg/m3)'],
        #     row['PM10(mg/m3)'],
        #     row['TEMPERATURE(℃)'],
        #     row['HUMIDITY(%)'],
        #     row['WIND_SPEED(m/sec)'],
        #     row['VOC(ppb)'],
        #     row['WIND_DIRECT(degrees)']
        # ]



def aggregateData(dataDevice, newAggregate):

        porjects = pd.read_csv(dataDevice, parse_dates=["TIME"])
        data_aggregated = porjects.resample("15T",
                                            on="TIME").agg({"PM2_5(μg/m3)": ['sum', 'min', 'max', 'std'],
                                                                "PM10(mg/m3)":  ['sum', 'min', 'max', 'std'],
                                                                "TEMPERATURE(℃)":  ['sum', 'min', 'max', 'std'],
                                                                "HUMIDITY(%)":  ['sum', 'min', 'max', 'std'],
                                                                "VOC(ppb)":  ['sum', 'min', 'max', 'std'],
                                                                })
        
        data_aggregated.to_csv(newAggregate)


folders_756 = ['756-01', '756-04', '756-07']
folders_1032 = ['1032-01', '1032-04', '1032-07']

# 遍歷每個資料夾，對其中的檔案執行aggregateData函式
for folder_name in folders_756:
    folder_path = os.path.join('/path/to/your/root/folder', folder_name)  # 替換成你實際的根資料夾路徑
    files_in_folder = os.listdir(folder_path)
    for file_name in files_in_folder:
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            new_aggregate_path = os.path.join('/path/to/save/aggregate', f'{file_name}_aggregated.csv')  # 替換成你想要存放聚合檔案的路徑
            aggregateData(file_path, new_aggregate_path)






