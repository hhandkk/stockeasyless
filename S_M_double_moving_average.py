import csv
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

import utils
import utils_ui

"""
信号监控：
1、60天均线斜率
2、30天斜率为正
3、15天斜率为正
4、5天斜率在
5、2天斜率

选取策略：
【1】斜率形态：↗， ↘  ，→ ,︵,︶, ,╯,╮,╭,╰,
【2】m5 < m15
【3】取 m15 - m5 最小值 
"""
#定义策略输出对象
output_data=pd.DataFrame()
output_data["code"]=""
output_data["weight"]=0

#读取全部股票数据
current_date = datetime.date.today().__str__()
stock_list=utils.get_stock_list("2024-04-12")
print("code:"+ str(stock_list[1][0]))
for i in stock_list:
    # 读取数据近6个月股票数据
    print("i:"+ str(i))
    data = utils.get_sig_stock_by_date_in_db(i[0], "2024-01-01", current_date)

    # 增加均线和均线斜率
    if data.shape[0] < 60:
        continue
    data = utils.double_moving_average_Slope(data)
    # 输出明细数据
    print(i[0])
    data.to_csv(f"E:\python_data\py20240414\{i[0]}.csv")

    print("ok")
    # 监控策略：
    # m5 < m15
    # Slope_5_MA > Slope_15_MA
    # Slope_5_MA 、Slope_15_MA、Slope_60_MA > 0
    # 记录 Slope_5_MA - Slope_15_MA
    if data['Slope_5_MA'].iloc[i] > 0 and data['Slope_15_MA'].iloc[i] > 0 and data['Slope_60_MA'].iloc[i] > 0:
        if data['5_MA'].iloc[i] < data['15_MA'].iloc[i] and data['Slope_5_MA'].iloc[i] > data['Slope_15_MA'].iloc[i]:
            output_data.loc[len(output_data)]=[data['code'].iloc[i],data['15_MA'].iloc[i] - data['5_MA'].iloc[i]]

output_data['code'] = output_data['code'].astype(str)
output_data.to_csv("double_moving_average_Slope.csv")
# print(data["date"].iloc[0])
# data['date'] = pd.to_datetime(data['date'])
# data['close']=pd.to_numeric(data['close'])
# data = data.sort_values('date')  # 按日期排序
# data.set_index('date', drop=False)
# data.to_csv("history_A_stock_k_data.csv", index=False)
# print(type(data["close"][3]))
# print(data["close"].tolist())

#utils_ui.show_by_plot(plt,data,"close","blue",0.5,data["date"].iloc[0],data["date"].iloc[59],"stock")
# 计算均线和斜率
#result = double_moving_average_Slope(data)


# plt.figure(figsize=(20, 10))   #画布的大小
# plt.plot(data["date"],data['close'], label='Close Price', color='blue',linewidth= 0.5)
# plt.subplots_adjust(left=0.03, right=0.995, bottom=0.04, top=0.97)
# plt.xlim(datetime.datetime.strptime("2024-01-10", "%Y-%m-%d"),datetime.datetime.strptime("2024-4-12", "%Y-%m-%d"))
# plt.ylim(9, 11)
# plt.grid(True, axis='both', color='grey', linestyle='--', linewidth=0.5)
# plt.title('Dual Moving Average Strategy')
# plt.legend()
# plt.show()
