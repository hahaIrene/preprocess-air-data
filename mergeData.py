import pandas as pd
import os


def dataMerge(data_path, output_file, project):
    projects = []
    # project_1032 = []

    for fileName in os.listdir(data_path):
        fileSplit = fileName.split('_')
        if fileSplit[0] == str(project):
            projects.append(fileName)

    data = []
    for fileName in projects:
        subPath = os.path.join(data_path, fileName)
        newdata = pd.read_csv(subPath)
        data.append(newdata)
        
        # print(len(data))

    mergeData = pd.concat(data, axis=0)
    # rename columns
    # new_column = {
    #     'PM2_5(μg/m^3)': 'PM2_5(μg/m3)',
    #     'VOC()': 'VOC(ppb)'
    # }
    # mergeData.rename(columns=new_column, inplace=True)
    
    mergeData.to_csv(output_file) 


if __name__ == "__main__":
    months = ["01", "04", "07"]
    for month in months:
        data_path = f"./data/00_KSIOT_2021{month}"
        output_file_756 = f"./newoutput/{month}_756_merge.csv"
        output_file_1032 = f"./newoutput/{month}_1032_merge.csv"

        dataMerge(data_path, output_file_756, 756)
        dataMerge(data_path, output_file_1032, 1032)

