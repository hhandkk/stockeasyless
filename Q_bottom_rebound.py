#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
本程序模拟连续N=3天阴跌，第N+1=4天：
（1）回阳，大阳线 ，涨幅M>4：√
（2）小阳线，T型
（3）小阴线，大成交量

"""


import baostock as bs
import pandas as pd


def judge_kline_category(code, startdate, enddate):
    """判断证券在起止时间内的每日 K 线类别：阳线，阴线。
    免费、开源证券数据平台
    :param code:证券代码
    :param startdate:起始日期
    :param enddate:截止日期
    :return:
    """
    login_result = bs.login(user_id='anonymous', password='123456')
    print(login_result.error_msg)
    # 获取股票日 K 线数据,adjustflag 复权状态(1：后复权， 2：前复权，3：不复权）
    # 交易状态(1：正常交易 0：停牌）
    # frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据
    rs = bs.query_history_k_data(code,
                                 "date,code,open,high,low,close,tradeStatus,volume,pctChg",
                                 start_date=startdate,
                                 end_date=enddate,
                                 frequency="d", adjustflag="3")
    # 打印结果集
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        result_list.append(rs.get_row_data())
    df_init = pd.DataFrame(result_list, columns=rs.fields)
    # 剔除停盘数据
    df_status = df_init[df_init['tradeStatus'] == '1']
    df_status['open'] = df_status['open'].astype(float)
    df_status['high'] = df_status['high'].astype(float)
    df_status['low'] = df_status['low'].astype(float)
    df_status['close'] = df_status['close'].astype(float)
    df_status['volume'] = df_status['volume'].astype(float)
    df_status['pctChg'] = df_status['pctChg'].astype(float)
    df_status['kline_category'] = df_status.apply(
        lambda x: judge_function(x.open, x.close), axis=1)
    df_status.to_csv('df.csv')
    return df_status

def kline_application(df, N, M , L):
    """已知证券在起止时间内的每日 K 线类别：阳线，阴线。
    做如下统计：
    情景 1. 若证券股价连续 N 天下跌后出现大阳线，次日股价开盘上涨的次数
   （第 N+2 天）
    情景 2. 若证券股价连续 N 天上涨之后出现大阴线，次日股价开盘下跌的次数
   （第 N+2 天）
    :return:
    """
    daycounts = df.shape[0]  #行数
    df['kline_numb'] = [1 if x == 'positive' else 0 for x in
                        df['kline_category']]
    df['scene'] = 0
    df['scene1'] = 0
    df['scene2'] = 0
    total_counts = 0  # 计算情景 1 中证券股价连续 N 天下跌后出现大阳线的次数
    total_counts_1_sub = 0  # 计算情景 1 出现的次数:高开
    total_counts_2_sub = 0  # 计算情景 2 出现的次数：第二天继续阳线
    total_counts_3_sub = 0  # 计算情景 2 出现的次数：第二天阴线，L = 5个交易日内收盘价超过

    print("test" + str(df.iloc[2, 8]))  #涨跌幅
    for i in range(0, daycounts - N - 1):
        kline_numb_counts = 0
        for j in range(0, N):
            kline_numb_counts += df.iloc[i + j, 10]  #0是跌，1是涨
        if kline_numb_counts == 0 and df.iloc[i + N, 10] == 1 and df.iloc[i + N, 8] >= M:
            # 表明该证券连续 N 天下跌后出现了大阳线 ,涨幅大于M = 3
            total_counts += 1
            if df.iloc[i + N + 1, 2] > df.iloc[i + N, 5]:
                total_counts_1_sub += 1
                df.iloc[i + N, 11] = 1  # 表明这一天属于情景 1,高开
            if df.iloc[i + N + 1, 5] > df.iloc[i + N, 5]:
                total_counts_2_sub += 1
                df.iloc[i + N, 12] = 1  # 表明这一天属于情景 2,继阳
            if df.iloc[i + N + 1, 5] < df.iloc[i + N, 5] :
                for k in range(0, L):
                    if i + N + 1 + k + 1 >= daycounts:
                        continue
                    if df.iloc[i + N + 1 + k + 1, 5] >= df.iloc[i + N, 5]:
                        total_counts_3_sub += 1
                        df.iloc[i + N + 1 + k + 1, 12] = 1  # 表明这一天属于情景 3,回本
                        break
    df.to_csv('df2.csv')
    print("证券代码：" + df['code'][0])
    print("证券股价连续 N 天下跌后出现大阳线的总次数：" +
          str(total_counts))
    if total_counts == 0:
        return
    print("若证券股价连续 N 天下跌后出现大阳线，次日股价开盘上涨的次数（第N + 2天）:" + str(total_counts_1_sub) + ", 占比："
                                              + str(total_counts_1_sub / total_counts))

    print("若证券股价连续 N 天下跌后出现大阳线，次日股价上涨的次数（第N + 2天）:" + str(total_counts_2_sub) + ", 占比："
                                              + str(total_counts_2_sub / total_counts))

    print("若证券股价连续 N 天下跌后出现大阳线，次日股价下跌后，L天回本次数:" + str(total_counts_3_sub) + ", 上涨和回本共计占比："
          + str((total_counts_2_sub + total_counts_3_sub) / total_counts))
    return (total_counts, total_counts_1_sub,total_counts_2_sub,total_counts_3_sub)


def judge_function(open, close):
    if open > close:
        return 'negative'
    else:
        return 'positive'
if __name__ == '__main__':
        code = "sz.002281"
        startdate = "2000-01-01"
        enddate = "2024-04-05"
        N = 3
        M = 4
        L = 5
        df = judge_kline_category(code, startdate, enddate)
        kline_application(df, N,M,L)