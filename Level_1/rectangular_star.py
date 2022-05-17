# https://mulkkog.tistory.com/8?category=1261175

a, b = map(int, input().strip().split(' '))	# '5 3'을 입력시 ' '로 구별되며 정수형으로 저장됨

for i in range(b):		# 세로의 길이
    print('*' * a)		# 가로의 길이