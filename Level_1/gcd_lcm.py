# https://mulkkog.tistory.com/37?category=1261175

import math


def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = gcd * (n / gcd) * (m / gcd)

    answer = [gcd, lcm]

    return answer