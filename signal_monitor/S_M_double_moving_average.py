
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

"""
信号监控：
1、60天均线斜率
2、30天斜率为正
3、15天斜率为正
4、5天斜率在
5、2天斜率

选取策略：
【1】斜率都大于零
【2】m5 < m15
【3】取 m15 - m5 最小值 
"""

def double_moving_average_Slope(data):

     #计算均线
    data['2_MA'] = data['close'].rolling(window=2, min_periods=1).mean()
    data['5_MA'] = data['close'].rolling(window=5, min_periods=1).mean()
    data['15_MA'] = data['close'].rolling(window=15, min_periods=1).mean()
    data['30_MA'] = data['close'].rolling(window=30, min_periods=1).mean()
    data['60_MA'] = data['close'].rolling(window=60, min_periods=1).mean()
    #计算斜率
    data["Slope_2_MA"] = data["2_MA"].diff()
    data["Slope_5_MA"] = data["2_MA"].diff()
    data["Slope_15_MA"] = data["15_MA"].diff()
    data["Slope_30_MA"] = data["30_MA"].diff()
    data["Slope_60_MA"] = data["60_MA"].diff()

    return data

# 读取数据
data = pd.read_csv('000001.csv')  # 请替换成你的数据文件路径
#1 获取股票清单

#2 获取近4个月股票数据

# 对数据进行预处理（可选）
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# 计算均线和斜率
result = double_moving_average_Slope(data)

