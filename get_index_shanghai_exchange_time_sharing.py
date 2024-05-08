
import requests
import json
import utils
import config

import numpy as np

#封装成块
def get_index_shanghai_exchange_time_sharing_det():
    #1、取数
    #设置请求的头
    #请求东方财富获取数据
    #返回非标准json，预处理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url=config.getConfig()["url"]["index_shanghai_exchange_time_sharing"]
    res = requests.get(url,headers)

    result = res.text.split("jQuery35105528496742689353_1715096473681")[1].split("(")[1].split(");")[0]
    result_json = json.loads(result)
    #2、存储到mysql
    #utils.save_quote_txn(result_json['data']['diff'])
    #print(result_json)
    #转成二维数组
    #result_value_matrix=utils.jsonlist2matrix(result_json['data']['trends'])
    prePrice = result_json['data']['prePrice']  # 昨天收盘价
    date = result_json['data']['trends'][0][:10]
    print(result_json['data']['trends'])
    print(str(prePrice))
    print(date)
    #utils.save_quote_txn_bath(result_value_matrix)
    data_list = np.insert(result_json['data']['trends'], 0, date, axis=1)
    print(data_list)
get_index_shanghai_exchange_time_sharing_det()