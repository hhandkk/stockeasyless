
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

"""
�źż�أ�
1��60�����б��
2��30��б��Ϊ��
3��15��б��Ϊ��
4��5��б����
5��2��б��

ѡȡ���ԣ�
��1��б�ʶ�������
��2��m5 < m15
��3��ȡ m15 - m5 ��Сֵ 
"""

def double_moving_average_Slope(data):

     #�������
    data['2_MA'] = data['close'].rolling(window=2, min_periods=1).mean()
    data['5_MA'] = data['close'].rolling(window=5, min_periods=1).mean()
    data['15_MA'] = data['close'].rolling(window=15, min_periods=1).mean()
    data['30_MA'] = data['close'].rolling(window=30, min_periods=1).mean()
    data['60_MA'] = data['close'].rolling(window=60, min_periods=1).mean()
    #����б��
    data["Slope_2_MA"] = data["2_MA"].diff()
    data["Slope_5_MA"] = data["2_MA"].diff()
    data["Slope_15_MA"] = data["15_MA"].diff()
    data["Slope_30_MA"] = data["30_MA"].diff()
    data["Slope_60_MA"] = data["60_MA"].diff()

    return data

# ��ȡ����
data = pd.read_csv('000001.csv')  # ���滻����������ļ�·��
#1 ��ȡ��Ʊ�嵥

#2 ��ȡ��4���¹�Ʊ����

# �����ݽ���Ԥ������ѡ��
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# ������ߺ�б��
result = double_moving_average_Slope(data)

