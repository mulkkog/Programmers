# https://mulkkog.tistory.com/33?category=1261175

import math


def solution(n):
    sqrt = math.sqrt(n)

    if int(sqrt) * int(sqrt) == n:
        return pow(sqrt + 1, 2)

    else:
        return -1