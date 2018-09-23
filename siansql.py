import pymysql
import sys

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
    sql += 'where node=%s'%node
  sql += 'limit %d,%d'%((page - 1) * num + 1, page * num)
  try:
    cursor.execute(sql)
    res = cursor.fetchall()
  except:
    print(sys.exc_info())
  con.close()
  print(res)
  return res