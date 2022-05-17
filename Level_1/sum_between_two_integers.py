# https://mulkkog.tistory.com/34?category=1261175

def solution(a, b):
    if a == b:
        return a
    else:
        return sum(range(min(a,b), max(a,b)+1))