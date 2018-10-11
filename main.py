#!/usr/bin/python3
#coding:utf-8
import sinasql
import requestmethod
import time
if requestmethod.isHoliday(time.strftime("%Y%m%d", time.localtime())):
    print('休息日：不需爬取')
else:
    print('工作日：需要爬取')
    num = 20

    # 矫正时间，处理为xx:30或者xx:00,t_hour为小时，t_min为分
    t = time.localtime()
    if t.tm_min < 15 or t.tm_min > 45:
        t_min = '00'
        if t.tm_min > 45:
            t_hour = t.tm_hour + 1
        else:
            t_hour = t.tm_hour
    else:
        t_min = '30'
        t_hour = t.tm_hour
    now = '%d-%02d-%02d %s:%s:00'%(t.tm_year,t.tm_mon,t.tm_mday,t_hour,t_min)
    # now = '2018-10-10 10:30:00'
    print('当前矫正后的时间为%s'%now)

    nodes = ['sh_a','sh_b','sz_a','sz_b','dpzs']
    for node in nodes:
        page = 1
        while True:
            symbols = sinasql.getSymbols(page, num, node)
            if len(symbols) == 0 :
                break
            data = requestmethod.getDetail(symbols)
            arr = []
            for i in range(len(data)):
                arr.append((symbols[i],now,data[i][1],data[i][2],data[i][4],data[i][5],data[i][8]))
            # 代号，时间，今开，昨收，最高，最低，成交量
            sql = 'insert into ' + node + ' (symbol,day,open,close,high,low,volume) values (%s,%s,%s,%s,%s,%s,%s)'
            sinasql.saveList(sql, arr)
            print('->请求数据成功，当前页数:%s当前时间：%s,当前节点：%s\n'%(page, now, node))
            if num != len(symbols):
                break
            page += 1
