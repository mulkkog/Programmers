# https://mulkkog.tistory.com/27?category=1261175

def solution(s):
    s = list(s)

    s.sort(reverse=True)	# 역순으로 정렬
    answer = ''.join(s)		# (공백 없이) s의 요소를 붙여 문자열로 만듬

    return answer