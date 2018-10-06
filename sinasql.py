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
    sql = 'select MAX(day) from %s '%node
    print(sql)
    cursor.execute(sql)
    day = cursor.fetchone()[0]
    print(day)
    sql = 'SELECT name, %s.* from %s left join NodeList on %s.symbol=NodeList.symbol where day=\'%s\' limit %d,%d'%(node, node, node, day,(page-1) * num, num)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data) > 0:
      sql = 'select count(*) from NodeList where node=\'%s\''%(node)
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

def getHistory(node, symbol, showType='hours', length='30'):
  if not (node and symbol):
    return json.dumps({'error': True, 'err_msg': '缺少参数'})
  print('%s,%s,%s,%s'%(node, symbol, showType, length))
  length = int(length)
  con,cursor = dbCon()
  try:
    if showType == 'hours':
      sql = 'select * from %s where symbol=\'%s\' ORDER BY day DESC limit %d'%(node, symbol, length)
    else:
      # 这句我还没想好怎么写
      sql = 'select * from %s where symbol=\'%s\' ORDER BY day DESC limit %d'%(node, symbol, length)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    sql = 'select name from NodeList where symbol = \'%s\''%symbol
    cursor.execute(sql)
    name = cursor.fetchone()[0]
    res = { 'error': False, 'name': name, 'data': data }
  except:
    print(sys.exc_info()[1])
    res = { 'error': True, 'err_msg': '内部错误' }
  con.close()
  return json.dumps(res)