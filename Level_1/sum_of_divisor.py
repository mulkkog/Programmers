# https://mulkkog.tistory.com/39?category=1261175

from math import isqrt

def solution(n):
    answer = 0

    for i in range(1, isqrt(n) + 1):		# 1

        if (n % i) == 0:			# 2
            answer += i
            if i != (n // i):			# 3
                answer += (n // i)

    return answer