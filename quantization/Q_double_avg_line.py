import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ����˫���߲��Ժ���
def dual_moving_average_strategy(data, short_window=20, long_window=50):
    # ������ھ��ߺͳ��ھ���
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # ���ɽ����ź�
    data['Signal'] = 0  # ��ʼ���ź���
    data['Signal'][short_window:] = \
        np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    # �����ھ����ϴ����ھ���ʱ�����루�ź�Ϊ1���������������ź�Ϊ0��

    # ����ֱֲ仯
    data['Position'] = data['Signal'].diff()

    return data

# ��ȡ����
data = pd.read_csv('your_data_file.csv')  # ���滻����������ļ�·��

# �����ݽ���Ԥ������ѡ��
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Ӧ��˫���߲���
result = dual_moving_average_strategy(data)

# ���ӻ����
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
