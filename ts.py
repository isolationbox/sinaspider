import tushare as ts
#import sinasql
ts.set_token('65323b72477636e0b2bc6e4fb40d47629a5a1da1a48dadafb24199c2')
pro = ts.pro_api()
list1 = ['sh000002','sh000003','sh000008','sh000009','sh000010','sh000011','sh000012','sh000016','sh000017','sh000300','sz399001','sz399002','sz399003','sz399004','sz399005','sz399006','sz399100','sz399101','sz399106','sz399107','sz399108','sz399333','sz399606']
for item in list1:
    if item[0:2] == 'sh':
        key = '000%s.SH'%item[-3:]
    else:
        key = '399%s.SZ'%item[-3:]
    print(key)
    df = pro.index_daily(ts_code=key,start_date='20180801',end_date='20180930')
    c_len = df.shape[0]
    for i in range(c_len):
        try:
            arr = (list(df.iloc[i]))
            with open('dp_mock.sql', 'a+') as f:
                f.write('insert into stock_day_line values (\'%s\',\'%s\',%s,%s,%s,%s,%s,%s,%s,%s,%s);\n'%(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9],arr[10]))
        except:
            print('%d error\n'%i)
        #sinasql.saveList('insert into stock_day_line (`code`, `date`, `open`, `high`, `low`, `close`, `pre_close`, `change_num`, `pct_change`, `vol`, `amount`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', arr)