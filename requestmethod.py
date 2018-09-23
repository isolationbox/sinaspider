import urllib.request
import urllib.error
import re

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

def getDetail(data):
    try:
        url = 'http://hq.sinajs.cn/list=' + ','.join(data)
        html = urllib.request.urlopen(url)
        res = html.read().decode('gbk')
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
            return []
    else:
        return list(map(lambda v: v.split(','),re.sub(r'var .*?"','',res).replace('";','').split('\n')[0:-1]))
