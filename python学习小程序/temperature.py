#!/usr/bin/env python
#华氏温度转换为摄氏温度
fahrenheit = 0
print(input("Fahrenheit Celsius"))
while fahrenheit <= 250:
    celsius = (fahrenheit - 32)/1.8   #转换
    print("{:5d} {:7.2f}".format(fahrenheit,celsius))
    fahrenheit += 25
