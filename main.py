import siansql
import requestmethod

symbols = siansql.getSymbols(1,20,'all')
print(requestmethod.getDetail(symbols))
