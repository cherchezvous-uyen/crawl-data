import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('champions.csv')

# Lưu dữ liệu vào file Excel
df.to_excel('champions.xlsx', index=False)
