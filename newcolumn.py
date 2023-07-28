import pandas as pd


def newcolumn(data_path):

    oldData = pd.read_csv(data_path)

    new_column = {
        'PM2_5(μg/m^3)':'PM2_5(μg/m3)',
        'VOC()':'VOC(ppb)'
    }

    oldData.rename(columns=new_column, inplace=True)
    oldData.to_csv(data_path, index=False)


if __name__ == "__main__":
    months = ["01", "04", "07"]
    for month in months:
        data_path_756 = f"./output/{month}_756_merge.csv"
        data_path_1032 = f"./output/{month}_1032_merge.csv"
        
        newcolumn(data_path_756)
        newcolumn(data_path_1032)
        

