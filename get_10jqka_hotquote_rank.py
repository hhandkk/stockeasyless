
import requests
import json
import datetime
import utils
import config

#1、取数
#设置请求的头
#请求东方财富获取数据
#返回非标准json，预处理
headers = {
        'User-agent': "Mozilla 5.10",
        'cache-control': "no-cache",
        'postman-token': "220d2989-c111-fea3-874f-f5c31113db59"
}

url=config.getConfig()["url"]["quote_10jqka_hotrank"]
print(url)
print(headers)
res = requests.get(url,headers=headers)
#result_json = json.loads(res.text)
print(res)
result_text= res.text
print(result_text)
#2、存储到mysql
#utils.save_quote_txn(result_json['data']['diff'])

