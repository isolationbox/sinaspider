import siansql
import requestmethod

page = 1
num = 20
while True:
    symbols = siansql.getSymbols(page, num, 'all')
    if len(symbols) == 0 :
        break
    data = requestmethod.getDetail(symbols)
    arr = []
    for i,v in enumerate(data):
        arr.append((symbols[i],v[0],v[3],v[6],v[7],v[2],v[1],v[4],v[5],v[8],v[9]))
    # 代号，名称，最新价，买入，卖出，昨收，今开，最高，最低，成交量(股票数，一般要除100)，成交额(元，一般除万)
    sql = 'insert into detail (symbol,name,price,buy,sell,settlement,open,high,low,volume,amount) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    siansql.saveList(sql, arr)
    if num != len(symbols):
        break
    page += 1