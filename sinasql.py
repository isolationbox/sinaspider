#!/usr/bin/python3
#coding:utf-8
import pymysql
import sys
import json

def dbCon():
  con = pymysql.connect(host='localhost',user='sinaspider',password='123456', database='sinaspider')
  cursor = con.cursor()
  return con, cursor

def saveList(sql, list):
  con, cursor = dbCon()
  try:
    cursor.executemany(sql, list)
    con.commit()
  except:
    con.rollback()
    print(sys.exc_info())
  con.close()

def getSymbols(page, num = 20, node='all'):
  con,cursor = dbCon()
  sql = 'select symbol from NodeList'
  if node != 'all':
    sql += ' where node=\'%s\''%node
  sql += ' limit %d,%d'%((page - 1) * num, num)
  try:
    cursor.execute(sql)
    result = cursor.fetchall()
    res = list(map(lambda v: v[0], result))
  except:
    res = []
    print(sys.exc_info())
  con.close()
  return res

def getLastInfoByNode(node='dpzs', page=1 , num=20):
  print('%s,%s,%s'%(node,page,num))
  page = int(page)
  num = int(num)
  con,cursor = dbCon()
  try:
    sql = 'select MAX(date) from stock_day_line left join NodeList on stock_day_line.code = NodeList.code where NodeList.node=\'%s\''%node
    print(sql)
    cursor.execute(sql)
    date = cursor.fetchone()[0]
    print(date)
    sql = 'SELECT NodeList.name,stock_day_line.* FROM stock_day_line LEFT JOIN NodeList ON stock_day_line.code = NodeList.code WHERE NodeList.node = \'%s\' and stock_day_line.date =\'%s\' limit %d,%d'%(node,date,(page-1)*num,num)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data) > 0:
      sql = 'select count(*) from stock_day_line LEFT JOIN NodeList ON stock_day_line.code = NodeList.code where NodeList.node=\'%s\' and date = \'%s\''%(node,date)
      cursor.execute(sql)
      total = cursor.fetchone()[0]
    else:
      total = 0
    res = { 'error': False, 'data': data,'total': total}
  except:
    print(sys.exc_info()[1])
    res = { 'error': True, 'err_msg': '内部错误' }
  con.close()
  return json.dumps(res)

def getHistory(code, num=30):
  print('%s,%s'%(code,num))
  num = int(num)
  con,cursor = dbCon()
  try:
    sql = 'select * from stock_day_line where code=\'%s\' order by date limit %d'%(code,num)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    res = { 'error': False, 'data': data }
  except:
    print(sys.exc_info()[1])
    res = { 'error': True, 'err_msg': '内部错误' }
  con.close()
  return json.dumps(res)