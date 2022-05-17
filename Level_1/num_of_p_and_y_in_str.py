# https://mulkkog.tistory.com/24?category=1261175

def solution(s):
    small_p_count = s.count('p')	# p 개수
    big_p_count = s.count('P')		# P 개수
    small_y_count = s.count('y')	# y 개수
    big_y_count = s.count('Y')		# Y 개수

    if (small_p_count + big_p_count) == (small_y_count + big_y_count):	# 비교
        return True
    else:
        return False