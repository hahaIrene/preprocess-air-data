import pandas as pd
import os

# # 使用resample方法，指定"timestamp"欄位為時間索引，並將資料aggregate成15分鐘一筆，取資料的平均值（或其他適當的統計指標）
# df_aggregated = df.resample("15T", on="timestamp").mean()




def aggregateData(dataDevice, newAggregate):

        porjects = pd.read_csv(dataDevice, parse_dates=["TIME"])
        data_aggregated = porjects.resample("15T",
                                            on="TIME").agg({"PM2_5(μg/m3)": ['mean', 'min', 'max', 'std'],
                                                            "PM10(mg/m3)":  ['mean', 'min', 'max', 'std'],
                                                            "TEMPERATURE(℃)":  ['mean', 'min', 'max', 'std'],
                                                            "HUMIDITY(%)":  ['mean', 'min', 'max', 'std'],
                                                            "VOC(ppb)":  ['mean', 'min', 'max', 'std'],
                                                        })
        
        data_aggregated.to_csv(newAggregate)




folders_756 = ['756-01', '756-04', '756-07']
folders_1032 = ['1032-01', '1032-04', '1032-07']

for folder_name in folders_756:
    folder_path = os.path.join(r'./device', folder_name) 
#     列出來所有檔名！！！！再忘就是智障
    files_in_folder = os.listdir(folder_path)
    for file_name in files_in_folder:
        if file_name.endswith('.csv'):
            file_path_756 = os.path.join(folder_path, file_name)
            new_aggregate_756 = os.path.join(r'./agg15m', f'{file_name}_aggregated.csv') 
            aggregateData(file_path_756, new_aggregate_756)


for folder_name in folders_1032:
    folder_path = os.path.join(r'./device', folder_name) 
#     列出來所有檔名！！！！再忘就是智障
    files_in_folder = os.listdir(folder_path)
    for file_name in files_in_folder:
        if file_name.endswith('.csv'):
            file_path_1032 = os.path.join(folder_path, file_name)
            new_aggregate_1032 = os.path.join(r'./agg15m', f'{file_name}_aggregated.csv') 
            aggregateData(file_path_1032, new_aggregate_1032)





