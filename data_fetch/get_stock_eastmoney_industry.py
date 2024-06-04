import requests
import json
import utils
import config
import datetime
import uuid



##抓取单只股票行业
def get_stock_eastmoney_industry_by_code(code):
    #1、取数
    #设置请求的头
    #请求东方财富获取数据
    #返回非标准json，预处理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url=config.getConfig()["url"]["quote_easymoney_industry"].replace("stock_code",code)
    res = requests.get(url,headers)

    result = res.text
    result_json = json.loads(result)
    #2、存储到mysql
    #utils.save_quote_txn(result_json['data']['diff'])
    #print(result_json)
    #转成二维数组
    result_value_matrix=utils.jsonlist2matrix(result_json['result']['data'])
    date = datetime.date.today().__str__()
    data_matrix = [[date] + element for element in result_value_matrix ]
    print(data_matrix)
    print(date)
    ##utils.save_stock_eastmoney_concept_bath(date,data_matrix)


def get_stock_eastmoney_industry_by_code_2_matrix(date,code):
    #1、取数
    #设置请求的头
    #请求东方财富获取数据
    #返回非标准json，预处理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url=config.getConfig()["url"]["quote_easymoney_industry"].replace("stock_code",code)
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

def get_all_stock_eastmoney_industry():
    #1、取数,获取所有的股票，注意是交易日
    date = datetime.date.today().__str__()
    date = '2024-05-31'   #test

    # [code,name]
    stock_list_all = utils.get_stock_list(date)

    #先清理 当前数据 再分页执行插入
    utils.delete_stock_eastmoney_industry_bath(date)
    # 设定每页的数量
    page_size = 100
    # 计算总页数
    total_pages = len(stock_list_all) // page_size + (1 if len(stock_list_all) % page_size > 0 else 0)

    print("计算总页数:"+str(total_pages))
    # 循环遍历每一页
    for zssssszwx in range(total_pages):
        # 计算当前页的起始索引和结束索引
        start_index = page_number * page_size
        end_index = min((page_number + 1) * page_size, len(stock_list_all))

        # 打印当前页的数据
        page_data = stock_list_all[start_index:end_index]
        print(f"Page {page_number + 1}: {page_data}")

        concept_all_data = []
        # 循环遍历每一页数据
        for stock_obj in page_data:
            # 2、获取所有股票的概念数据
            # print(stock_obj[0])
            data_matrix = get_stock_eastmoney_industry_by_code_2_matrix(date, stock_obj[0])
            if not data_matrix:
                continue
            # if i[0] > "000010":break
            concept_all_data = concept_all_data + data_matrix
            #print(concept_all_data)
        utils.save_stock_eastmoney_industry_bath(date, concept_all_data)


get_all_stock_eastmoney_industry()