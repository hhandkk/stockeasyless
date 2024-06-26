import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义双均线策略函数
def dual_moving_average_strategy(data, short_window=5, long_window=22):
    # 计算短期均线和长期均线
    data['Short_MA'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    # 生成交易信号
    data['Signal'] = 0  # 初始化信号列
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    # 当短期均线上穿长期均线时，买入（信号为1），否则卖出（信号为0）


    # 计算持仓变化
    data['Position'] = data['Signal'].diff()
    #模拟1w元投资收益
    data['monitor']= 0
    money = 10000
    daycounts = data.shape[0]  # 行数
    buy_status = 0  # 买入状态
    stock_sum =0 # 股数
    print("1 " +str(data.iloc[2,5]))
    print("2 " +str(data.iloc[2,7]))
    for i in range(0, daycounts - 1):
        if data.iloc[i , 11] == 1:
            if buy_status == 0:
                stock_sum = money / data.iloc[i , 5]
                buy_status = 1
            data.iloc[i , 13] = stock_sum * data.iloc[i , 5]
        if data.iloc[i, 12] == -1:
            data.iloc[i, 13] = stock_sum * data.iloc[i, 5]
            money = stock_sum * data.iloc[i, 5]
            buy_status = 0
    data.to_csv('000001_return.csv')

    return data

# 读取数据
data = pd.read_csv('000001.csv')  # 请替换成你的数据文件路径

# 对数据进行预处理（可选）
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# 应用双均线策略
result = dual_moving_average_strategy(data)

# 可视化结果
plt.figure(figsize=(10, 5))
plt.plot(result['close'], label='Close Price', color='blue')
plt.plot(result['Short_MA'], label='Short MA', color='orange')
plt.plot(result['Long_MA'], label='Long MA', color='green')
plt.plot(result.loc[result['Signal'] == 1].index,
         result['Short_MA'][result['Signal'] == 1],
         '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(result.loc[result['Signal'] == -1].index,
         result['Short_MA'][result['Signal'] == -1],
         'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.title('Dual Moving Average Strategy')
plt.legend()
plt.show()
