import pandas as pd

# 读取数据
data = pd.read_csv('000001.csv')  # 请替换成你的数据文件路径

# 对数据进行预处理（可选）
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

aaa = data['close'][20:]
