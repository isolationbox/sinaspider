import siansql
import requestmethod
import time

num = 20
now = time.strftime("%Y-%m-%d %H", time.localtime())
nodes = ['sh_a', 'sh_b', 'sz_a', 'sz_b', 'dpzs']
for node in nodes:
    page = 1
    while True:
        symbols = siansql.getSymbols(page, num, node)
        if len(symbols) == 0 :
            break
        data = requestmethod.getDetail(symbols)
        arr = []
        for i,v in enumerate(data):
            arr.append((symbols[i],v[0],v[3],v[6],v[7],v[2],v[1],v[4],v[5],v[8],v[9],v[30],v[31],now))
        # 代号，名称，最新价，买入，卖出，昨收，今开，最高，最低，成交量(股票数，一般要除100)，成交额(元，一般除万),日期，时间，创建时间
        sql = 'insert into ' + node + ' (symbol,name,price,buy,sell,settlement,open,high,low,volume,amount,date,time,created) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        siansql.saveList(sql, arr)
        print('第%s请求成功\n'%page)
        if num != len(symbols):
            break
        page += 1