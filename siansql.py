#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

def dbCon():
  con = pymysql.connect(host='localhost',user='sinaspider',password='123456', database='sinaspider')
  cursor = con.cursor()
  return con, cursor

def saveList(sql, list):
  con, cursor = dbCon()
  try:
    print(list)
    cursor.executemany(sql, list)
    con.commit()
  except Exception:
    con.rollback()
    print(Exception)
  con.close()
