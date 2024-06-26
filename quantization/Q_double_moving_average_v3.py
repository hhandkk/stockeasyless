from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

def dual_moving_average_strategy(data, short_window=1, long_window=5,long_long_window= 30):
    # 计算短期均线和长期均线
    data['Short_MA'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    # 生成交易信号
    data['Signal'] = 0  # 初始化信号列
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    # 当短期均线上穿长期均线时，买入（信号为1），否则卖出（信号为0）


    # 计算持仓变化
    data['Position'] = data['Signal'].diff()
    #1投资收益走势
    data['monitor'] = 0
    #短均线斜率
    data["slope_short"] = data["Short_MA"].diff()
    # 长均线斜率
    data["slope_long"] = data["Long_MA"].diff()
    # 持股日期
    data["stock"] = 0
    data['Long_Long_MA'] = data['close'].rolling(window=long_window, min_periods=1).mean()
    data["slope_long_long"] = data["Long_MA"].diff()
    daycounts = data.shape[0]  # 行数
    buy_status = 0  # 买入状态
    stock_sum = 1 # 初始入场股数，1股
    money = data.iloc[0,5] #初始资金,第一天收盘价格1股
    print("1 " +str(data.iloc[2,5]))
    print("2 " +str(data.iloc[2,7]))
    for i in range(0, daycounts):
        # 如果未持股
        if buy_status == 0 :
            #判断金叉、长均线斜率大于0，买入
            if data.iloc[i, 11] == 1 and data.iloc[i, 15] >= 0 and data.iloc[i, 17] >= 0 :
                stock_sum = money / data.iloc[i, 5]
                buy_status = 1
                data.iloc[i, 16] =1
        #如果持股
        if buy_status == 1:
            # 判断短均线>长均线、短均线斜率大于0，继续持股
            if data.iloc[i, 11] == 1 and data.iloc[i, 14] >= 0:
                money = stock_sum * data.iloc[i , 5]
                data.iloc[i, 16] = 1
            #如果死叉、或者短期均线斜率小于0，则卖出
            if data.iloc[i, 12] == -1 or data.iloc[i, 14] < 0:
                money = stock_sum * data.iloc[i, 5]
                buy_status = 0
        data.iloc[i, 13] = money
    data.to_csv('000001_return.csv')

    return data

# 读取数据
data = pd.read_csv('000001.csv')  # 请替换成你的数据文件路径

# 对数据进行预处理（可选）
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# 应用双均线策略
result = dual_moving_average_strategy(data)
print("持股天数：" + str(data["stock"].sum()) + "持股比例："+ str(data["stock"].sum()/data.shape[0]))
# 可视化结果
plt.figure(figsize=(20, 10))   #画布的大小
plt.plot(result['close'], label='Close Price', color='blue',linewidth= 0.5)
plt.plot(result['Short_MA'], label='Short MA', color='orange',linewidth= 0.5)
plt.plot(result['Long_MA'], label='Long MA', color='green',linewidth= 0.5)
plt.plot(result['monitor'], label='monitor', color='red',linewidth= 0.8)
# plt.plot(result.loc[result['Signal'] == 1].index,
#           result['Short_MA'][result['Signal'] == 1],
#           '^', markersize=10, color='g', lw=0, label='Buy Signal')
# plt.plot(result.loc[result['Signal'] == -1].index,
#           result['Short_MA'][result['Signal'] == -1],
#           'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.subplots_adjust(left=0.03, right=0.995, bottom=0.04, top=0.97)
plt.xlim(datetime.strptime("2024-01-01", "%Y-%m-%d"),datetime.strptime("2024-04-12", "%Y-%m-%d"))
plt.grid(True, axis='both', color='grey', linestyle='--', linewidth=0.5)
plt.title('Dual Moving Average Strategy')
plt.legend()
plt.show()
