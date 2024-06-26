import time
import random

import requests
import json
import utils
import config
import datetime

#记录日志
log_url = config.getConfig()["parm"]["log_url"].replace("yyyy-mm-dd",datetime.date.today().__str__())
logger = utils.setup_logger(log_url)

#设置请求的头
#获取所有股票代码


stock_list_all = utils.get_stock_list(datetime.date.today().__str__())
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
start_date= "2024-04-09"
end_date= "2024-04-11"

insert_sum = 0;
result_matrix = []
# stock_list_all = [
#     ["000001", "平安银行"],
#     ["000002", "万 科A"]]
for i in stock_list_all:

    if i[0].startswith('60'):
        url_comm = config.getConfig()["url"]["quote_txn_req_history_url_sh"]
    elif i[0].startswith('00') or i[0].startswith('30'):
        url_comm = config.getConfig()["url"]["quote_txn_req_history_url_sz"]
    else:
        continue
    #拼接url


    url_stock = url_comm.replace("stockcode",i[0])
    #print(url_stock)
    #取数
    res = requests.get(url_stock,headers)
    #print(res.text.__str__())
    result = res.text.split("jsonp1711941323422")[1].split("(")[1].split(");")[0]
    result_json = json.loads(result)
    #print(result_json)
    #入库
    result_matrix_tmp = list(map(lambda i:i.split(",") ,result_json['data']['klines']))
    #print(result_matrix)
    #print(type(result_matrix[1]))
    for row in result_matrix_tmp:
        row.append(i[0])
        row.append(i[1])
    result_matrix.extend(result_matrix_tmp)
    print(i[0]+i[1])
    insert_sum = insert_sum + 1
# print(str(result_matrix))
utils.save_sig_stock_history_by_date(start_date,end_date,result_matrix)
#logger.info(start_date+"到"+ end_date+"入库完成。" )
#logger.info("共计入库" + str(insert_sum) + "个股票历史数据")

#拼接单个股票请求的url
#请求东方财富单个股票K线图ajax请求数据
#返回非标准json，预处理
#url=config.getConfig()["url"]["quote_txn_req_history_url"]
#res = requests.get(url,headers)
#print(res.text.__str__())
#result = res.text.split("jsonp1711606605952")[1].split("(")[1].split(");")[0]
#result_json = json.loads(result)



#2、存储到mysql
#result_matrix = list(map(lambda i:i.split(",") ,result_json['data']['klines']))
#print(result_matrix)
#print(type(result_matrix[1]))
#utils.save_sig_stock_history_bath(stock_code,stock_name,result_matrix)

# 2011-09-07,2.77,3.03,3.03,2.73,106618,306013072.00,11.07,11.81,0.32,58.58
# 日期f0，开盘f17，收盘f2，最高f15，最低f16，成交量f5，成交额f6，振幅%f7，涨跌幅%f3，涨跌额f4，换手率f8



