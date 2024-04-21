import pandas as pd

# 创建示例数据框
data = {'value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# 创建rolling对象并计算移动平均
rolling_mean = df['value'].rolling(window=3).mean()
print(rolling_mean)


import utils


pd = utils.get_sig_stock_by_date_in_db("000001","2024-01-10","2024-04-12")

pd.to_csv("aaa.csv")

#test