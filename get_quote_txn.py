
import requests
import json
import utils
import config

#1、取数
#设置请求的头
#请求东方财富获取数据
#返回非标准json，预处理
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
url=config.getConfig()["url"]["quote_txn_req_url"]
res = requests.get(url,headers)

result = res.text.split("jQuery112406326540387216384_1711515195823")[1].split("(")[1].split(");")[0]
result_json = json.loads(result)
#2、存储到mysql
#utils.save_quote_txn(result_json['data']['diff'])
#print(result_json)
#转成二维数组
result_value_matrix=utils.jsonlist2matrix(result_json['data']['diff'])
print(result_value_matrix)
utils.save_quote_txn_bath(result_value_matrix)

