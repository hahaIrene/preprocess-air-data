import pandas as pd
# # import os

# # def dataMerge(data_path, output_file):
# #     project_756 = []
# #     project_1032 = []

# #     for fileName in os.listdir(data_path):
# #         fileSplit = fileName.split('_')

# #         if fileSplit[0] == "756":
# #             project_756.append(fileName)

# #         elif fileSplit[0] == "1032":
# #             project_1032.append(fileName)

# #     data_756 = []
# #     for fileName in project_756:
# #         subPath = os.path.join(data_path, fileName)
# #         data = pd.read_csv(subPath)
# #         data_756.append(data)
# #     mergeData_756 = pd.concat(data_756, axis=0)
# #     mergeData_756.to_csv(output_file)

# #     data_1032 = []
# #     for fileName in project_1032:
# #         subPath = os.path.join(data_path, fileName)
# #         data = pd.read_csv(subPath)
# #         data_1032.append(data)
# #     mergeData_1032 = pd.concat(data_1032, axis=0)
# #     mergeData_1032.to_csv(output_file)

# # if __name__ == "__main__":
# #     months = ["01", "04", "07"]
# #     for month in months:
# #         data_path = f"./data/00_KSIOT_2021{month}"
# #         output_file_756 = f"./output/{month}_756_merge.csv"
# #         output_file_1032 = f"./output/{month}_1032_merge.csv"

# #         dataMerge(data_path, output_file_756)
# #         dataMerge(data_path, output_file_1032)


# import pandas as pd
# import os

# def dataMerge(data_path, output_file):
#     project_756 = []
#     project_1032 = []
    
#     for fileName in os.listdir(data_path):
#         fileSplit = fileName.split('_')

#         if fileSplit[0] == "756":
#             project_756.append(fileName)
#         elif fileSplit[0] == "1032":
#             project_1032.append(fileName)

#     data_756 = []
#     for fileName in project_756:
#         subPath = os.path.join(data_path, fileName)
#         data = pd.read_csv(subPath)
#         data_756.append(data)

#     mergeData_756 = pd.concat(data_756, axis=0)
#     mergeData_756.to_csv(output_file)

# if __name__ == "__main__":
#     months = ["01", "04", "07"]
#     for month in months:
#         data_path = f"./data/00_KSIOT_2021{month}"
#         output_file_756 = f"./output/{month}_756_merge.csv"
#         output_file_1032 = f"./output/{month}_1032_merge.csv"

#         dataMerge(data_path, output_file_756)
#         # dataMerge(data_path, output_file_1032)

data = pd.read_csv(r"./forDL/shuffled_data.csv")

X = data.head()
print(data.columns)