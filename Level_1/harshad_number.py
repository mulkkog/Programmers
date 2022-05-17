# https://mulkkog.tistory.com/12?category=1261175

def solution(x):
    digits_sum = 0

    for i in str(x):	# 문자열로 변경 후 한글자씩 접근
        digits_sum += int(i)	# 자릿수의 합에 더해준다

    if x%digits_sum == 0:	# 자릿수의 합이 처음 입력받은 수로 나눠지면 나머지가 0이다
        answer = True
    else:
        answer = False

    return answer