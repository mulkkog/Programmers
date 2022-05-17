# https://mulkkog.tistory.com/18?category=1261175

def solution(n):
    str_n = str(n)

    answer = 0

    for i in str_n:
        answer += int(i)

    return answer