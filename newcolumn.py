import pandas as pd


oldData = pd.DataFrame(data_path)

new_column = {
    'PM2_5(μg/m^3)':'PM2_5(μg/m3)',
    'VOC()':'VOC(ppb)'
}

oldData.rename(columns=new_column, inplace=True)



