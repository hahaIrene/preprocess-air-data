import pandas as pd

# 假設你有一個 DataFrame df
data = {
    'Old_Column_A': [1, 2, 3],
    'Old_Column_B': [4, 5, 6],
    'Old_Column_C': [7, 8, 9]
}
df = pd.DataFrame(data)

# 創建一個字典來對應舊的 column 名稱到新的 column 名稱
new_column_names = {
    'Old_Column_A': 'New_Column_A',
    'Old_Column_B': 'New_Column_B',
    'Old_Column_C': 'New_Column_C'
}

# 使用 rename() 函式更新 column 名稱
df.rename(columns=new_column_names, inplace=True)

# 輸出更新後的 DataFrame
print(df)




oldData = pd.DataFrame(data_path)

new_column




