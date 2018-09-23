#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.error

def getInfo(url, data):
    try:
        headers = { 'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0' }
        url += '?'
        for key in data.keys():
            url += (key + '=' + str(data[key]) + '&')
        response = urllib.request.Request(url ,headers= headers)
        html = urllib.request.urlopen(response)
        result = html.read().decode('gbk')
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
            return '[]'
    else:
        return result