#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import math

EPS = 1e-07


def sum_func(x):
    summa = 1.0
    temp = 0
    n = 1
    while abs(summa - temp) > EPS:
        temp = summa
        summa += math.sin(n*x) / n
        n += 1

    print(f"Sum is {summa}")


def check_func(x):
    res = - math.log(2 * math.sin(0.5 * x))
    print(f"Check: {res}")


if __name__ == '__main__':
    x = math.pi
    th1 = Thread(target=sum_func, args=(x,))
    th2 = Thread(target=check_func, args=(x,))
    th1.start()
    th2.start()
