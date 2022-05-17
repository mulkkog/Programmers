# https://mulkkog.tistory.com/19?category=1261175

def solution(s):
    s_split = s.split(' ')  # 공백을 기준으로 나누기 ['try', 'hello', 'world']

    answer = []  # 새로운 단어 담을 리스트

    for word in s_split:  # 단어 하나씩 보기
        print(word)
        new_word = ""  # 새로운 문자열 담을 곳

        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()  # 짝수일 경우 대문자
            else:
                new_word += word[i].lower()  # 홀수일 경우 소문자

        answer.append(new_word)  # 새로운 단어 추가

    return " ".join(answer)  # 구분자 " "를 넣어서 새로운 문자열로 만들기