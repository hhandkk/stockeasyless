
import requests
import json
import utils
import config
import datetime

#封装成块
def get_stock_eastmoney_concept_by_code(code):
    #1、取数
    #设置请求的头
    #请求东方财富获取数据
    #返回非标准json，预处理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url=config.getConfig()["url"]["quote_easymoney_concept"].replace("stock_code",code)
    res = requests.get(url,headers)

    result = res.text
    result_json = json.loads(result)
    #2、存储到mysql
    #utils.save_quote_txn(result_json['data']['diff'])
    #print(result_json)
    #转成二维数组
    result_value_matrix=utils.jsonlist2matrix(result_json['result']['data'])
    date = current_date = datetime.date.today().__str__()
    data_matrix = [[date] + element for element in result_value_matrix ]
    print(data_matrix)
    print(date)
    utils.save_stock_eastmoney_concept_bath(date,data_matrix)

def get_stock_eastmoney_concept_by_code_2_matrix(date,code):
    #1、取数
    #设置请求的头
    #请求东方财富获取数据
    #返回非标准json，预处理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url=config.getConfig()["url"]["quote_easymoney_concept"].replace("stock_code",code)
    res = requests.get(url,headers)

    result = res.text
    result_json = json.loads(result)
    #2、存储到mysql
    #utils.save_quote_txn(result_json['data']['diff'])
    #print(result_json)
    #转成二维数组
    if not result_json['result']:
        return ''
    result_value_matrix=utils.jsonlist2matrix(result_json['result']['data'])
    #date = current_date = datetime.date.today().__str__()
    data_matrix = [[date] + element for element in result_value_matrix ]
    return  data_matrix

def get_all_stock_eastmoney_concept():
    #1、取数,获取所有的股票，注意是交易日
    date = datetime.date.today().__str__()
    date = '2024-05-31'   #test
    #清理当天的数据
    utils.delete_stock_eastmoney_concept_bath(date)
    # [code,name]
    stock_list_all = utils.get_stock_list(date)
    concept_all_data = []
    #2、获取所有股票的概念数据
    record_num = 0;
    for i in stock_list_all:
        print(i[0])
        data_matrix = get_stock_eastmoney_concept_by_code_2_matrix(date,i[0])
        if not data_matrix:
            continue
        record_num = record_num + len(data_matrix)
        concept_all_data = concept_all_data + data_matrix
        if len(concept_all_data) > 1000:
            utils.save_stock_eastmoney_concept_bath(date, concept_all_data)
            concept_all_data = []
    utils.save_stock_eastmoney_concept_bath(date,concept_all_data)
    print("股票概念数据" + date + "共计入库" + record_num + "条！")

