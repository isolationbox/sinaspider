import tushare as ts
import sinasql
pro = ts.pro_api()
nodes = ['sh_a', 'sha_b', 'sz_a', 'sz_b']
for node in nodes:
    page = 1
    symbols = sinasql.getSymbols(page, 20, node)
    for symbol in symbols:
        code = symbol[4:] + '.SH' if symbol[2] == 'h' else '.SZ'
        print(code)
        df = pro.daily(ts_code=code, start_date='20180801', end_date='20180930')
        break
    print(df)
    print(list(df.iloc[0]))
    break

