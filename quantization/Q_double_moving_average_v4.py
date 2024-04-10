from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

def dual_moving_average_strategy(data, short_window=2, long_window=12,hold_date = 5):
    # 计算短期均线和长期均线
    data['OpenClose_MA'] = (data['open'] + data['close'])/2  #当天开盘和收盘平均价
    data['Short_MA'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['close'].rolling(window=long_window, min_periods=1).mean()
    #data['Short_MA'] = data['OpenClose_MA']
    # 生成交易信号
    data['Signal'] = 0  # 初始化信号列
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    # 当短期均线上穿长期均线时，买入（信号为1），否则卖出（信号为0）
    # 计算持仓变化,金叉1、死叉-1
    data['Intersection'] = data['Signal'].diff()
    #1股投资收益走势
    data['Earnings'] = 0
    #短均线斜率\# 长均线斜率
    data["Slope_short"] = data["Short_MA"].diff()
    data["Slope_long"] = data["Long_MA"].diff()
    data["Buy_point"] = 0;



    daycounts = data.shape[0]  # 行数
    buy_status = 0  # 买入状态
    stock_sum = 1 # 初始入场股数，1股
    money = data.iloc[0,5] #初始资金,第一天收盘价格1股
    print("1 " +str(data.iloc[2,5]))
    print("2 " +str(data.iloc[2,7]))
    for i in range(0, daycounts - hold_date):
        # 如果未持股
        if buy_status == 0:
            # 判断金叉、长均线斜率大于0，买入
            if data["Intersection"].iloc[i] == 1 and data["Slope_long"].iloc[i] >= 0:
                data["Buy_point"].iloc[i] = 1
                #用Earnings记录金叉后N天最大股价
                for j in range(1,hold_date):
                    if data["close"].iloc[i+j] > data["Earnings"].iloc[i]:
                        data["Earnings"].iloc[i] = data["close"].iloc[i+j]
    data.to_csv('000001_return_v3.csv')

    return data

# 读取数据
data = pd.read_csv('000001.csv')  # 请替换成你的数据文件路径

# 对数据进行预处理（可选）
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# 应用双均线策略
result = dual_moving_average_strategy(data)

#金叉、长均线斜率大于0的数量：
count_buy_point= data["Buy_point"].sum()
#买入后，最高收益点大于买入点的数量：
count_earn = np.where(data["Earnings"] > data["close"],1,0).sum()
#平均收益率：
count_earn_rate=np.where(data["Buy_point"] == 1,(data["Earnings"] - data["close"])/data["close"],0).sum() / count_buy_point

print("买入点数量：" + str(count_buy_point))
print("最高收益点大于买入点的数量：" + str(count_earn))
print("增值概率：" + str(count_earn / count_buy_point))
print("平均收益率：" + str(count_earn_rate))
