import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# 示例数据
dates = pd.date_range('20240101', periods=50)
opens = np.random.randint(100, 200, size=50)
highs = np.random.randint(200, 250, size=50)
lows = np.random.randint(50, 100, size=50)
closes = np.random.randint(100, 200, size=50)
volumes = np.random.randint(1000, 5000, size=50)

# 创建 DataFrame
data = pd.DataFrame({'Date': dates, 'Open': opens, 'High': highs, 'Low': lows, 'Close': closes, 'Volume': volumes})

# 设置日期格式
data['Date'] = pd.to_datetime(data['Date'])

# 计算涨跌颜色
colors = ['red' if data['Close'][i] > data['Open'][i] else 'green' for i in range(len(data))]

# 创建灯笼状 K 线图和成交量子图
fig, ax = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# 绘制K线
for i in range(len(data)):
    ax[0].plot([data['Date'][i], data['Date'][i]], [data['Low'][i], data['High'][i]], color='black', linewidth=1)
    ax[0].plot([data['Date'][i], data['Date'][i]], [data['Open'][i], data['Close'][i]], color=colors[i], linewidth=5)

# 绘制成交量
ax[1].bar(data['Date'], data['Volume'], color=colors)

# 计算股价平均线
data['Price_MA_60'] = data['Close'].rolling(window=60).mean()
data['Price_MA_15'] = data['Close'].rolling(window=15).mean()
data['Price_MA_5'] = data['Close'].rolling(window=5).mean()

# 计算成交量平均线
data['Volume_MA_60'] = data['Volume'].rolling(window=60).mean()
data['Volume_MA_15'] = data['Volume'].rolling(window=15).mean()
data['Volume_MA_5'] = data['Volume'].rolling(window=5).mean()

# 绘制股价平均线
ax[0].plot(data['Date'], data['Price_MA_60'], color='blue', label='Price MA 60')
ax[0].plot(data['Date'], data['Price_MA_15'], color='orange', label='Price MA 15')
ax[0].plot(data['Date'], data['Price_MA_5'], color='purple', label='Price MA 5')

# 绘制成交量平均线
ax[1].plot(data['Date'], data['Volume_MA_60'], color='blue', label='Volume MA 60')
ax[1].plot(data['Date'], data['Volume_MA_15'], color='orange', label='Volume MA 15')
ax[1].plot(data['Date'], data['Volume_MA_5'], color='purple', label='Volume MA 5')

# 设置x轴日期格式
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax[1].tick_params(axis='x', rotation=45)

# 添加标签
ax[0].set_title('Candlestick Chart with Volume and Moving Averages')
ax[1].set_xlabel('Date')
ax[0].set_ylabel('Price')
ax[1].set_ylabel('Volume')

# 添加图例
ax[0].legend()
ax[1].legend()

# 调整子图间距
plt.tight_layout()

# 显示图形
plt.show()
