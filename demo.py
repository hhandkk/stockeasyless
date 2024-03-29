import datetime
import json

import config

history_date = config.getConfig()["parm"]["history_date"]
print(type(history_date))
current_datetime = datetime.datetime.now()
current_hour = current_datetime.hour

print(current_hour)

#-----------------------------------------------------------------
data_list = [{"name": "Tom", "age": 18}, {"name": "Jerry", "age": 12}]

print(f"data_list 类型 : {type(data_list)} 值为 {data_list}")

# 将列表转为 json
json_str = json.dumps(data_list)
# 打印 json 字符串结果
print(f"json_str 类型 : {type(json_str)} 值为 {json_str}")

# 将 json 转为 Python 列表数据
data_list2 = json.loads(json_str)
xxxs  =  list(data_list2[1].values())
xxxsplus = list(map(lambda i:str(i) ,xxxs))
print(xxxsplus)
print(f"data_list2 类型 : {type(data_list2)} 值为 {data_list2}")

res = list(map(lambda i:list(map(lambda i:str(i),list(i.values()))) ,data_list2))
print("hello:")
print(res)

#-------------------------------------------------------------------------------------
print( datetime.datetime.now())

