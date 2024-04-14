import pandas as pd

import utils

# 读取数据
data = pd.read_csv('000001.csv')  # 请替换成你的数据文件路径

# 对数据进行预处理（可选）
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

aaa = data['close'][20:]



utils.stock_desc("000001").show_stock_desc()


pd = utils.get_sig_stock_by_date_in_db("000001","2024-01-10","2024-04-12")

pd.to_csv("aaa.csv")