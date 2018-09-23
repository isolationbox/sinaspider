#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.error
import demjson
import sql

def getInfo(url, data):
    try:
        headers = { 'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0' }
        url += '?'
        for key in data.keys():
            url += (key + '=' + str(data[key]) + '&')
        response = urllib.request.Request(url ,headers= headers)
        html = urllib.request.urlopen(response)
        result = html.read().decode('gb2312')
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('错误原因是' + str(e.reason))
            return '{}'
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
            return '{}'
    else:
        return result

url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'
data = {
    'page': 1,
    'num': 20,
    'sort': 'symbol',
    'asc': 1,
    'symbol': '',   
    '_s_r_a': 'init',
    'node': 'sh_a'
}
stockInfo = demjson.decode(getInfo(url, data))
for item in stockInfo:
    print(item)

