#!/usr/bin/env python
#计算10个数字的平均值
N = 10
sum = 0
count = 0
print("please input 10 number:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum/N
print("N={} Sum={}".format(N,sum))
print("Averagen = {:.2f}".format(average))
