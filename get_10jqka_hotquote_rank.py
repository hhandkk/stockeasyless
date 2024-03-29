
import requests
import json
import datetime
import utils
import config

#1、取数
#设置请求的头
#请求东方财富获取数据
#返回非标准json，预处理
headers = {"Access-Control-Allow-Headers":"Content-Type",
"Access-Control-Allow-Methods":"*",
"Access-Control-Allow-Origin":"*",
"Access-Control-Max-Age":"1800",
"Connection":"keep-alive",
"Content-Encoding":"gzip",
"Content-Type":"application/json",
"Date":"Thu, 28 Mar 2024 04:44:17 GMT",
"Server":"openresty",
"Transfer-Encoding":"chunked",
"Vary":"Accept-Encoding",
"Via":"1.1 cachemd215220.10jqka.com.cn (squid/3.5.20), 1.1 cachefsdx12 (squid/3.5.20)",
"X-Cache":"MISS from cachemd215220.10jqka.com.cn",
"X-Cache":"MISS from cachefsdx12",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding":"gzip, deflate, br, zstd",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"spversion=20130314; historystock=605333%7C*%7C002875%7C*%7C603290%7C*%7C688230%7C*%7C603019; Hm_lvt_722143063e4892925903024537075d0d=1709081695,1709701381,1711328447; Hm_lvt_929f8b362150b1f77b477230541dbbc2=1709081696,1709701384,1711328448; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1709016844,1709081696,1709701381,1711328448; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=zuGjZy0G8E%2BQrchgQv%2Fnlvrk33KYgcFt3DN8dCfQl%2B4g3KrUprXhOikfMDVHXghN%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D; u_did=9C20C5AD55D645F68D29C4925ED2365E; u_ttype=WEB; user=MDptb18yMDE4MDgzNjk6Ok5vbmU6NTAwOjIxMTgwODM2OTo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoyNDo6OjIwMTgwODM2OToxNzExNDQ5OTc1Ojo6MTQxNTc2NTUyMDo2MDQ4MDA6MDoxZjdiOTFlNGNhY2FmZDEwMDc2ZDljMmI4ZmQ1Njg0Njc6ZGVmYXVsdF80OjE%3D; userid=201808369; u_name=mo_201808369; escapename=mo_201808369; ticket=1b2eb15bf853ce284604a0ffaf9d2727; user_status=0; utk=ace76d4e3c31a948bcdcab4dddfeead2; v=AxF0T932EyIIFn82y80FQI-NIBaufoZnL_opNvOmCF73kT9IO86VwL9COcOA",
"Host":"dq.10jqka.com.cn",
"Sec-Ch-Ua":"Google Chrome;v=123, Not:A-Brand;v=8, Chromium;v=123",
"Sec-Ch-Ua-Mobile":"?1",
"Sec-Ch-Ua-Platform":"Android",
"Sec-Fetch-Dest":"document",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"none",
"Sec-Fetch-User":"?1",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"}

url=config.getConfig()["url"]["quote_10jqka_hotrank"]
print(url)
print(headers)
res = requests.get(url,headers)
#result_json = json.loads(res.text)
print(res)
#2、存储到mysql
#utils.save_quote_txn(result_json['data']['diff'])

