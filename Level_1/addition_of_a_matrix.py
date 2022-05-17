# https://mulkkog.tistory.com/11?category=1261175

def solution(arr1, arr2):
    answer = []

    for i, lst in enumerate(arr1):  # arr1 리스트의 순서: i, 내용: lst  ex) 0 [1, 2]
        new = [x+y for x, y in zip(lst, arr2[i])]   # 각 요소들의 값 더하기
        answer.append(new)  # 정답 리스트에 추가

    return answer