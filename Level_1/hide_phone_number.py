# https://mulkkog.tistory.com/10?category=1261175

def solution(phone_number):
    answer = '*' * (len(phone_number) - 4)  # 전화번호의 길이에서 4를 제외한 숫자만큼 *추가
    answer += phone_number[-4:]  # 전화번호 뒷자리 4자리 추가

    return answer