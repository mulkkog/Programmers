# https://mulkkog.tistory.com/14?category=1261175

def solution(n):

    num_list = list(str(n))         # 들어온 정수를 문자열로 바꾼 후 다시 리스트로(한문자씩) 바꿈
    num_list.sort(reverse = True)	# 리스트에서 제공하는 정렬 함수 사용

    answer = int("".join(num_list))	# 묹자열을 다시 리스트로

    return answer