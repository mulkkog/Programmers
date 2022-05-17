# https://mulkkog.tistory.com/38?category=1261175

def solution(arr):

    answer = []
    tmp = None		# 마지막으로 answer 리스트에 추가된 원소

    for i in arr:
        if tmp == i:
            pass
        else:
            answer.append(i)
            tmp = i

    return answer