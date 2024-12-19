#문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오.
# 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

T = int(input())
"""
2
I am happy today
We want to win the first prize
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
<output>
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
"""

# 문자열 받아서 리스트로 변환 -> split
# 각 인덱스 순서변경
new_sentence = ""
for i in range(T):
    sentence = input().split()
    """sentence=["I", "am", "happy", "today"]"""
    new_sentence = []
    for j in sentence:
        new_sentence.append(j[::-1])
    answer = " ".join(new_sentence)
    print(answer)
