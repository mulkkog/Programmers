# https://mulkkog.tistory.com/9?category=1261175

def solution(arr):
    arr_count = len(arr)            # 리스트 안에 원소 개수
    arr_sum = sum(arr)              # 리스트 합계 계산

    answer = arr_sum / arr_count    # 평균 구하기

    return answer