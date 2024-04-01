import config
import requests
import json
import numpy


def get_column(array, column_index):
    return [row[column_index] for row in array]


url_comm = config.getConfig()["url"]["quote_txn_req_history_url"]
url_stock = url_comm.replace("stockcode","600001")
    #print(url_stock)
    #取数
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res = requests.get(url_stock,headers)

    #print(res.text.__str__())
result = res.text.split("jsonp1711941323422")[1].split("(")[1].split(");")[0]
result_json = json.loads(result)
    #print(result_json)
    #入库
result_matrix = list(map(lambda i:i.split(",") ,result_json['data']['klines']))
# 日期f0，开盘f17，收盘f2，最高f15，最低f16，成交量f5，成交额f6，振幅%f7，涨跌幅%f3，涨跌额f4，换手率f8

print(result_matrix)

dates=get_column(result_matrix,0)
opens=get_column(result_matrix,1)
closes = get_column(result_matrix,2)
highs= get_column(result_matrix,3)
lows =get_column(result_matrix,4)
volumes = get_column(result_matrix,5)

np_matrix= numpy.array(result_matrix)
k_matrix=np_matrix[:,0:6]
print(k_matrix)
