#!/usr/bin/python3
#coding:utf-8
import demjson
import sinasql
import requestmethod
import sys

nodeList = ["sh_a", "sh_b", "sz_a", "sz_b","dpzs"]
url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'

for node in nodeList:
    data = {
        'page': 1,
        'num': 100,
        'sort': 'symbol',
        'asc': 1,
        'symbol': '',   
        '_s_r_a': 'init',
    }
    data['node'] = node
    tryNum = 0
    while True:
        try:
            stockInfo = demjson.decode(requestmethod.getInfo(url, data))
        except:
            print(sys.exc_info())
            tryNum += 1
            if tryNum < 4:
                continue
            else:
                break
        sql = 'insert into  NodeList (symbol,name,node) values (%s,%s,%s)'
        data['page'] += 1
        data['_s_r_a'] = 'page'
        params = list(map(lambda item: (item['symbol'], item['name'],node), stockInfo))
        sinasql.saveList(sql, params)
        if len(stockInfo) < 100:
            break
