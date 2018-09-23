import siansql
import requestmethod

symbols = siansql.getSymbols(1,20,'all')
data = requestmethod.getDetail(symbols)
print(data)