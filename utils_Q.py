
#线性拟合函数
#拟合斜率形态：↗， ↘  ，→ ,︵,︶, ,╯,╮,╭,╰,
#1固定斜率上涨：↗
#2固定斜率下跌：↘
#3直线横盘：→
#4抛物线加速上涨：╯
#5抛物线加速下跌：╮
#6抛物线减速上涨（见顶）：╭
#7抛物线减速下跌（减低）：╰
#8抛物线过顶下跌：︵
#9抛物线过底上涨：︶

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#输入一个完整pd
def linear_fitting(data,num):
    data_samp = data.head(num)
    data_samp.reset_index(drop=True, inplace=True)
    data_samp['index'] = range(59, -1, -1)
    data_samp.to_csv("tmp.csv")
    #使用二次方程来拟合60天均线
    x=data_samp['index']
    y=data_samp['60_MA']
    params = np.polyfit(x, y , 1)
    print("parms:" + str(params))
    #构造一个多项式
    param_func = np.poly1d(params)
    #比较
    y_predict = param_func(x)
    plt.scatter(x, y)
    plt.plot(x, y_predict)
    plt.ylim(0, 11)
    plt.show()

data = pd.read_csv('000001.csv')
linear_fitting(data,60)

