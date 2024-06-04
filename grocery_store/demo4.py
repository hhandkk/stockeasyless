import datetime

import numpy as np
import matplotlib.pyplot as plt

import utils

# x是一个数组，在-5~5，等间距生成的50个点
x = np.linspace(-5, 5, 50)
# 假造y，为sin(x)，同时加上一些噪声，模拟真实世界的数据
y = np.sin(x) + np.random.rand(50)
x.shape, y.shape
((50,), (50,))
plt.scatter(x, y)



# 使用三次方多项式做拟合
params = np.polyfit(x, y, 10)

param_func = np.poly1d(params)


y_predict = param_func(x)
plt.scatter(x, y)
plt.plot(x, y_predict)

#-------------------------
current_date = datetime.date.today().__str__()
stock_list=utils.get_stock_list("2024-04-19")

data = utils.get_sig_stock_by_date_in_db("603557", "2024-01-01", current_date)
data = utils.double_moving_average_Slope(data)
data = data.sort_values("date",ascending=False,inplace=False)
    # 输出明细数据
data.to_csv("E:\python_data\py20240414\py603557_tmp.csv")

