# https://mulkkog.tistory.com/13?category=1261175

def solution(num):
    count = 0  # 작업 횟수를 세는 변수

    while num != 1:  # 입력된 수가 1이 아닐때 계속 실행
        count += 1  # 작업 횟수 +1

        if count > 501:  # 작업 횟수가 500이 넘으면 -1로 변경 후 리턴
            count = -1
            break

        if num % 2 == 0:  # 짝수라면 2로 나눈다
            num /= 2
        else:  # 홀수라면 3을 곱하고 1을 더한다
            num = (num * 3) + 1

    return count  # 작업 횟수 리턴