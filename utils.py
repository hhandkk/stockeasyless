import datetime
import mysql
import config

#---------------------------------------------------------------------------
#股票每日交易数据入库
#一天两次，日中一次、日终一次
#入库前，先删除当天存量试点数据
def save_quote_txn(data):
    # 6、清理当天的数据
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    delete_sql = "delete from quote_price_txn where f0 = %s and f1= %s"
    mysql.delete_data(delete_sql, (current_date,f1_point))
    print(current_date + f1_point + "数据删除成功。")
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    for i in data:
        f0 = current_date
        f1 = f1_point
        f2 = str(i['f2'])
        f3 = str(i['f3'])
        f4 = str(i['f4'])
        f5 = str(i['f5'])
        f6 = str(i['f6'])
        f7 = str(i['f7'])
        f8 = str(i['f8'])
        f9 = str(i['f9'])
        f10 = str(i['f10'])
        f11 = str(i['f11'])
        f12 = str(i['f12'])
        f13 = str(i['f13'])
        f14 = str(i['f14'])
        f15 = str(i['f15'])
        f16 = str(i['f16'])
        f17 = str(i['f17'])
        f18 = str(i['f18'])
        f20 = str(i['f20'])
        f21 = str(i['f21'])
        f22 = str(i['f22'])
        f23 = str(i['f23'])
        f24 = str(i['f24'])
        f25 = str(i['f25'])
        f62 = str(i['f62'])
        f115 = str(i['f115'])
        f128 = str(i['f128'])
        f140 = str(i['f140'])
        f141 = str(i['f141'])
        f136 = str(i['f136'])
        f152 = str(i['f152'])
        f200 = current_date
        insert_sql = "insert quote_price_txn(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f62,f115,f128,f140,f141,f136,f152,f200) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        val = (f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f62,f115,f128,f140,f141,f136,f152,f200)
        mysql.insert_or_update_data(insert_sql, val)
        print(val.__str__() + "入库成功。")
    #输出入库情况
    print(current_date + f1_point + "股票明细已经入库，共计" + len(data) +"条数据。")

#--------------------------------------------------------------------------------------------------
def jsonlist2matrix(data):
    return list(map(lambda i:list(i.values()) ,data))
    #嵌套强转str
    #return list(map(lambda i:list(map(lambda i:str(i),list(i.values()))) ,data))
#--------------------------------------------------------------------------------------------------
#批量提取当前股票明细
def save_quote_txn_bath(data):
    # 6、清理当天的数据
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    delete_sql = "delete from quote_price_txn where f0 = %s and f1= %s"
    mysql.delete_data(delete_sql, (current_date,f1_point))
    print(current_date + f1_point + "数据删除成功。")
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    insert_sql = "insert quote_price_txn(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f62,f115,f128,f140,f141,f136,f152) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    mysql.insert_data_bath(insert_sql,data)
    #print(val.__str__() + "入库成功。")
    #输出入库情况
    ##更新f0、f1,f200
    update_sql = "update quote_price_txn set f0= %s ,f1 = %s,f200 = %s where f0 is null"
    val=(current_date,f1_point,datetime.datetime.now().__str__())
    mysql.insert_or_update_data(update_sql,val)
    print(current_date + f1_point + "股票明细已经入库，共计" + str(len(data)) + "条数据。")

#--------------------------------------------------------------------------------------------------
#批量提取当前股票明细
def save_sig_stock_history_bath(stock_code,stock_name,data):
    # 6、清理该个股历史数据
    f1_point = "日末"
    history_date = config.getConfig()["parm"]["history_date"]

    delete_sql = "delete from quote_price_txn where f12 = %s and f0 <= %s"
    mysql.delete_data(delete_sql, (stock_code,history_date))
    print(stock_code +"股票数据"+ str(history_date) +"前的数据全部删除成功。")
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    insert_sql = "insert quote_price_txn(f0,f17,f2,f15,f16,f5,f6,f7,f3,f4,f8) values (%s,%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
    mysql.insert_data_bath(insert_sql,data)
    #print(val.__str__() + "入库成功。")
    #输出入库情况
    ##更新f0、f1,f200
    update_sql = "update quote_price_txn set f1 = %s,f12 = %s,f14 = %s,f200 = %s where f0 <= %s and f12 is null"
    val=(f1_point,stock_code,stock_name,datetime.datetime.now().__str__(),history_date)
    mysql.insert_or_update_data(update_sql,val)
    print(stock_code +stock_name+ "历史股票明细已经入库，共计" + str(len(data)) + "条数据。")

#-----------------------------------------------------------------------------------------------------------------
#
#20240329
#获取股票清单
def get_stock_list(val_date):
    select_sql = "select distinct f12,f14 from quote_price_txn where f0 = %s"
    result_list=list(mysql.query_data(select_sql,val_date))
    return result_list


#-------------------------------------------------------------------------------------------------------------
#记录日志

import logging


def setup_logger(log_file):
    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # 创建一个logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 创建一个文件handler，用于写入日志文件
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 创建一个控制台handler，用于输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


# 示例用法
if __name__ == "__main__":
    logger = setup_logger('app.log')
    logger.info('程序开始运行')
    # 运行中的代码
    logger.info('程序结束运行')


#--------------------------------------------------------------------------------------------------
def clean_10jqka_hotquote():
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    delete_sql = "delete from stock_10jqka_hotrank where date = %s and data_point= %s"
    mysql.delete_data(delete_sql, (current_date, f1_point))
    print(current_date + f1_point + "同花顺排行数据删除成功。")

#批量获取同花顺排行榜
def save_10jqka_hotquote(data):
    # 6、清理当天的数据
    f1_point = "日中"
    if  datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    #insert_sql = "insert stock_10jqka_hotrank(date，order，market，code，rate，rise_and_fall，name，analyse，hot_rank_chg，concept_tag，popularity_tag，analyse_title，data_point，data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #mysql.insert_data_bath(insert_sql,data)


    date = current_date
    order = str(data["order"])
    market = str(data["market"])
    code = str(data["code"])
    rate = str(data["rate"])
    rise_and_fall = str(data["rise_and_fall"])
    name = str(data["name"])
    analyse = data.get("analyse", "")
    hot_rank_chg = str(data["hot_rank_chg"])
    concept_tag = str(data["tag"]["concept_tag"])
    try:
        popularity_tag = str(data["tag"]["popularity_tag"])
    except KeyError:
        popularity_tag=""
    analyse_title = data.get("analyse_title", "")
    data_point = str(f1_point)
    data_time = datetime.datetime.now().__str__()
    insert_sql = "insert stock_10jqka_hotrank(date,rank_order,market,stock_code,rate,rise_and_fall,stock_name,analyse,hot_rank_chg,concept_tag,popularity_tag,analyse_title,data_point,data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (date,order,market,code,rate,rise_and_fall,name,analyse,hot_rank_chg,concept_tag,popularity_tag,analyse_title,data_point,data_time)
    print(val)
    mysql.insert_or_update_data(insert_sql, val)
    print(name + f1_point + "排行数据入库成功。")
    #输出入库情况


#--------------------------------------------------------------------------------------------------
def clean_10jqka_skyrocket():
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    delete_sql = "delete from stock_10jqka_skyrocket where date = %s and data_point= %s"
    mysql.delete_data(delete_sql, (current_date, f1_point))
    print(current_date + f1_point + "同花顺飙升排行数据删除成功。")

#批量获取同花顺排行榜
def save_10jqka_skyrocket(data):
    # 6、清理当天的数据
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    #insert_sql = "insert stock_10jqka_hotrank(date，order，market，code，rate，rise_and_fall，name，analyse，hot_rank_chg，concept_tag，popularity_tag，analyse_title，data_point，data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #mysql.insert_data_bath(insert_sql,data)


    date = current_date
    order = str(data["order"])
    market = str(data["market"])
    code = str(data["code"])
    rate = str(data["rate"])
    rise_and_fall = str(data["rise_and_fall"])
    name = str(data["name"])
    analyse = data.get("analyse", "")
    hot_rank_chg = str(data["hot_rank_chg"])
    concept_tag = str(data["tag"]["concept_tag"])
    try:
        popularity_tag = str(data["tag"]["popularity_tag"])
    except KeyError:
        popularity_tag=""
    analyse_title = data.get("analyse_title", "")
    data_point = str(f1_point)
    data_time = datetime.datetime.now().__str__()
    insert_sql = "insert stock_10jqka_skyrocket(date,rank_order,market,stock_code,rate,rise_and_fall,stock_name,analyse,hot_rank_chg,concept_tag,popularity_tag,analyse_title,data_point,data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (date,order,market,code,rate,rise_and_fall,name,analyse,hot_rank_chg,concept_tag,popularity_tag,analyse_title,data_point,data_time)
    print(val)
    mysql.insert_or_update_data(insert_sql, val)
    print(name + f1_point + "飙升排行数据入库成功。")
    #输出入库情况



#--------------------------------------------------------------------------------------------------
def clean_10jqka_concept():
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    delete_sql = "delete from stock_10jqka_concept where date = %s and data_point= %s"
    mysql.delete_data(delete_sql, (current_date, f1_point))
    print(current_date + f1_point + "热点概念排行数据删除成功。")

#批量获取同花顺排行榜
def save_10jqka_concept(data):
    # 6、清理当天的数据
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    #insert_sql = "insert stock_10jqka_hotrank(date，order，market，code，rate，rise_and_fall，name，analyse，hot_rank_chg，concept_tag，popularity_tag，analyse_title，data_point，data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #mysql.insert_data_bath(insert_sql,data)


    date = current_date

    etf_product_id = str(data.get("etf_product_id", ""))
    code = str(data.get("code", ""))
    rate = str(data.get("rate", ""))
    rise_and_fall = str(data.get("rise_and_fall", ""))
    etf_rise_and_fall = str(data.get("etf_rise_and_fall", ""))
    name = str(data.get("name", ""))
    hot_rank_chg = str(data.get("hot_rank_chg", ""))
    market_id = str(data.get("market_id", ""))
    hot_tag = str(data.get("hot_tag", ""))
    tag = str(data.get("tag", ""))
    etf_market_id = str(data.get("etf_market_id", ""))
    order = str(data.get("order", ""))
    data_point = str(f1_point)
    data_time = datetime.datetime.now().__str__()
    insert_sql = ("insert stock_10jqka_concept(date,etf_product_id,concept_code,rate,etf_rise_and_fall,rise_and_fall,concept_name,hot_rank_chg,market_id,hot_tag,concept_tag,etf_market_id,eft_order,data_point,data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")

    val = (date,etf_product_id,code,rate,rise_and_fall,etf_rise_and_fall,name,hot_rank_chg,market_id,hot_tag,tag,etf_market_id,order ,data_point,data_time)
    print(val)
    mysql.insert_or_update_data(insert_sql, val)
    print(name + f1_point + " 概念热版数据入库成功。")
    #输出入库情况




#--------------------------------------------------------------------------------------------------
def clean_10jqka_industry():
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    delete_sql = "delete from stock_10jqka_industry where date = %s and data_point= %s"
    mysql.delete_data(delete_sql, (current_date, f1_point))
    print(current_date + f1_point + "热点概念排行数据删除成功。")

#批量获取同花顺排行榜
def save_10jqka_industry(data):
    # 6、清理当天的数据
    f1_point = "日中"
    if datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9 :
        f1_point = "日末"
    current_date = datetime.date.today().__str__()
    #股票代码,股票名称,最新价,涨跌幅,涨跌额,成交量（手）,成交额,振幅,换手率,市盈率,量比,最高,最低,今开,昨收,市净率等等
    #insert_sql = "insert stock_10jqka_hotrank(date，order，market，code，rate，rise_and_fall，name，analyse，hot_rank_chg，concept_tag，popularity_tag，analyse_title，data_point，data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #mysql.insert_data_bath(insert_sql,data)


    date = current_date

    etf_product_id = str(data.get("etf_product_id", ""))
    code = str(data.get("code", ""))
    rate = str(data.get("rate", ""))
    rise_and_fall = str(data.get("rise_and_fall", ""))
    etf_rise_and_fall = str(data.get("etf_rise_and_fall", ""))
    name = str(data.get("name", ""))
    hot_rank_chg = str(data.get("hot_rank_chg", ""))
    market_id = str(data.get("market_id", ""))
    hot_tag = str(data.get("hot_tag", ""))
    tag = str(data.get("tag", ""))
    etf_market_id = str(data.get("etf_market_id", ""))
    order = str(data.get("order", ""))
    data_point = str(f1_point)
    data_time = datetime.datetime.now().__str__()
    insert_sql = ("insert stock_10jqka_industry(date,etf_product_id,concept_code,rate,etf_rise_and_fall,rise_and_fall,concept_name,hot_rank_chg,market_id,hot_tag,concept_tag,etf_market_id,eft_order,data_point,data_time) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")

    val = (date,etf_product_id,code,rate,rise_and_fall,etf_rise_and_fall,name,hot_rank_chg,market_id,hot_tag,tag,etf_market_id,order ,data_point,data_time)
    print(val)
    mysql.insert_or_update_data(insert_sql, val)
    print(name + f1_point + " 行业热榜数据入库成功。")
    #输出入库情况

