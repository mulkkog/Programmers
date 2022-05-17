# https://mulkkog.tistory.com/4?category=1261175

def solution(arr):
    arr.remove(min(arr))  # 제일 작은 수 제거

    if not arr:  # 빈 Sequence(String / Tuple / List)는 False 값을 가진다
        arr.append(-1)  # 빈 리스트일 경우 -1 추가

    return arr