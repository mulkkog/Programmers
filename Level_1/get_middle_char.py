# https://mulkkog.tistory.com/31?category=1261175

def solution(s):
    quotient = len(s) // 2
    remainder = len(s) % 2

    if remainder != 0:
        answer = s[quotient]
    else:
        answer = s[quotient - 1] + s[quotient]

    return answer