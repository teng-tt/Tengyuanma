#!/usr/bin/env python
#计算投资金额盈利
amount = float(input("Enter amount:"))  #输入金额
inrate = float(input("Enter Interest rate:")) #输入利率
period = float(input("Enter period:")) #输入年限
value = 0
year = 1
while year <= period:
    value = amount + (inrate*amount)
    print("Year {} Rs.{:.2f}".format(year,value))
    year += 1
