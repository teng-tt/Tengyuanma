#!/usr/bin/env python
#猜数字游戏
guess = float(input("please input your guess:"))
if guess < 100:
    print("You guess is smaller than equal to 100")
elif guess == 100:
    print("Your guess is guessing")
else:
    print("Your guess is greater than 100")

