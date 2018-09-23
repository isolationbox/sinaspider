#!/usr/bin/python
# -*- coding: UTF-8 -*-
import demjson
import siansql
import requestmethod

nodeList = ["sh_a", "sh_b", "sz_a", "sz_b","hs_a","hs_b"]
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
    while True:
        try:
            stockInfo = demjson.decode(requestmethod.getInfo(url, data))
        except Exception:
            break
        sql = 'insert into  NodeList (symbol,name,node) values (%s,%s,' + node + ')'
        data['page'] += 1
        data['_s_r_a'] = 'page'
        params = list(map(lambda item: (item['symbol'], item['name']), stockInfo))
        siansql.saveList(sql, params)
        if len(stockInfo) < 100:
            break


