#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.error
import demjson
import siansql

def getInfo(url, data):
    try:
        headers = { 'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0' }
        url += '?'
        for key in data.keys():
            url += (key + '=' + str(data[key]) + '&')
        response = urllib.request.Request(url ,headers= headers)
        html = urllib.request.urlopen(response)
        result = html.read().decode('gb2312')
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
            return '[]'
    else:
        return result

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
            stockInfo = demjson.decode(getInfo(url, data))
        except Exception:
            break
        sql = 'insert into  NodeList (symbol,name,node) values (%s,%s,' + node + ')'
        data['page'] += 1
        data['_s_r_a'] = 'page'
        params = list(map(lambda item: (item['symbol'], item['name']), stockInfo))
        siansql.saveList(sql, params)
        if len(stockInfo) < 100:
            break


