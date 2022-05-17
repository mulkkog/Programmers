# https://mulkkog.tistory.com/16?category=1261175

def solution(n):
    answer = []  # 정답 리스트

    for i in str(n):  # 입력받은 정수를 문자열로 생각해서
        answer.append(int(i))  # 하나씩 가져온 후 다시 정수로 바꿔서 리스트에 추가

    answer.reverse()  # 리스트 뒤집기

    return answer