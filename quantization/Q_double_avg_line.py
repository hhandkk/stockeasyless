import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 定义双均线策略函数
def dual_moving_average_strategy(data, short_window=20, long_window=50):
    # 计算短期均线和长期均线
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # 生成交易信号
    data['Signal'] = 0  # 初始化信号列
    data['Signal'][short_window:] = \
        np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    # 当短期均线上穿长期均线时，买入（信号为1），否则卖出（信号为0）

    # 计算持仓变化
    data['Position'] = data['Signal'].diff()

    return data

# 读取数据
data = pd.read_csv('your_data_file.csv')  # 请替换成你的数据文件路径

# 对数据进行预处理（可选）
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# 应用双均线策略
result = dual_moving_average_strategy(data)

# 可视化结果
plt.figure(figsize=(10, 5))
plt.plot(result['Close'], label='Close Price', color='blue')
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
